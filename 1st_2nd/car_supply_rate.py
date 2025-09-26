# car_supply_rate.py
import pandas as pd
import requests
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

# -------------------------
# 1. 환경변수 로드 & DB 연결
# -------------------------
load_dotenv()
engine = create_engine(
    f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:3306/{os.getenv('DB_NAME')}?charset=utf8mb4"
)

# -------------------------
# 2. 스키마/테이블 초기화
# -------------------------
with engine.connect() as conn:
    conn.execute(text("DROP SCHEMA IF EXISTS mobilitydb"))
    conn.execute(text("CREATE SCHEMA mobilitydb DEFAULT CHARACTER SET utf8mb4"))
    conn.execute(text("USE mobilitydb"))

    conn.execute(text("""
        CREATE TABLE CAR_REGIST_SIDO (
            reg_date   VARCHAR(6),
            sido       VARCHAR(50),
            sigungu    VARCHAR(50),
            car_type   VARCHAR(20),
            usage_type VARCHAR(20),
            count      INT
        )
    """))

    conn.execute(text("""
        CREATE TABLE CAR_SUPPLY_RATE (
            period      VARCHAR(6),
            sido        VARCHAR(50),
            sigungu     VARCHAR(50),
            car_type    VARCHAR(20),
            usage_type  VARCHAR(20),
            count       INT,
            population  BIGINT,
            supply_rate FLOAT
        )
    """))

print("✅ mobilitydb 스키마 초기화 & 테이블 생성 완료")

# -------------------------
# 3. 차량 등록 데이터 (2011~)
# -------------------------
print("🚗 차량 등록 데이터 불러오는 중...")

API_KEY = "4c49d1028d634c258ca4c7b99eb4a134"
MOLIT_URL = "http://stat.molit.go.kr/portal/openapi/service/rest/getList.do"

params = {
    "key": API_KEY,
    "form_id": 5498,
    "style_num": 2,
    "start_dt": 201101,
    "end_dt": 202512
}

response = requests.get(MOLIT_URL, params=params)
response.raise_for_status()
data = response.json()

df = pd.DataFrame(data["result_data"]["formList"])
print("원본 컬럼:", df.columns.tolist())

df["reg_date"] = df["date"].astype(str).str[:6]

value_cols = [c for c in df.columns if any(x in c for x in ["승용", "승합", "화물", "특수"])]

long_df = df.melt(
    id_vars=["reg_date", "시도명", "시군구"],
    value_vars=value_cols,
    var_name="category",
    value_name="count"
)
long_df[["car_type", "usage_type"]] = long_df["category"].str.split(">", expand=True)

veh_final = long_df.rename(columns={
    "시도명": "sido",
    "시군구": "sigungu"
})[["reg_date", "sido", "sigungu", "car_type", "usage_type", "count"]]

veh_final["count"] = pd.to_numeric(veh_final["count"], errors="coerce").fillna(0).astype(int)

veh_final = veh_final[
    (veh_final["usage_type"] != "계") &
    (veh_final["sigungu"] != "계") &
    (veh_final["sido"] != "계")
].copy()

print("✅ 차량 데이터:", len(veh_final), "rows")

# -------------------------
# 4. 인구 데이터 (총인구만)
# -------------------------
print("👥 인구 데이터 불러오는 중...")

pop_path = os.path.join(os.path.dirname(__file__), "population_total_filtered.csv")

# ✅ CP949 인코딩으로 읽기
pop_df = pd.read_csv(pop_path, encoding="cp949")

print("✅ 인구 데이터:", len(pop_df), "rows")
print("인구 데이터 컬럼:", pop_df.columns.tolist())

# 긴 형태로 변환
pop_long = pop_df.melt(
    id_vars=["행정구역별(읍면동)", "항목", "단위"],
    var_name="year",
    value_name="population"
)

# 연도 숫자만 추출
pop_long["year"] = pop_long["year"].str.extract(r"(\d{4})").astype(int)

# 시도 / 시군구 분리
sido_sigungu = pop_long["행정구역별(읍면동)"].str.split(" ", n=1, expand=True)
pop_long["sido"] = sido_sigungu[0]
pop_long["sigungu"] = sido_sigungu[1]

# ⚠️ sigungu 없는 행(광역시/도 전체 합계) 제거
pop_long = pop_long[pop_long["sigungu"].notna()].copy()

# period 생성 (연도 + 월, 월은 차량데이터에 맞춰 1~12 모두 생성)
pop_final = []
for _, row in pop_long.iterrows():
    for month in range(1, 13):
        pop_final.append({
            "period": f"{row['year']}{str(month).zfill(2)}",
            "sido": row["sido"],
            "sigungu": row["sigungu"],
            "population": row["population"]
        })

pop_final = pd.DataFrame(pop_final)

print("✅ 인구 데이터 정제 완료:", len(pop_final), "rows")
print(pop_final.head(10))

# -------------------------
# 5. 병합 및 보급률 계산
# -------------------------
merged = pd.merge(
    veh_final,
    pop_final,
    left_on=["reg_date", "sido", "sigungu"],
    right_on=["period", "sido", "sigungu"],
    how="inner"
)

merged["supply_rate"] = (merged["count"] / merged["population"]) * 1000

print("✅ 보급률 계산 완료:", len(merged), "rows")
print(merged.head(10))

# -------------------------
# 6. DB 저장
# -------------------------
veh_final.to_sql("CAR_REGIST_SIDO", con=engine, if_exists="append", index=False, schema="mobilitydb")
merged.to_sql("CAR_SUPPLY_RATE", con=engine, if_exists="append", index=False, schema="mobilitydb")

print("✅ CAR_REGIST_SIDO 테이블 저장 완료")
print("✅ CAR_SUPPLY_RATE 테이블 저장 완료")
