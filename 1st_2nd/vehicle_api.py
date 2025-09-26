# vehicle_api.py
import pandas as pd
import requests
from sqlalchemy import create_engine
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
# 2. 차량 등록 데이터 (2011~)
# -------------------------
print("🚗 차량 등록 데이터 불러오는 중...")

API_KEY = "4c49d1028d634c258ca4c7b99eb4a134"
MOLIT_URL = "http://stat.molit.go.kr/portal/openapi/service/rest/getList.do"

params = {
    "key": API_KEY,
    "form_id": 5498,
    "style_num": 2,
    "start_dt": 201101,
    "end_dt": 202508
}

response = requests.get(MOLIT_URL, params=params)
response.raise_for_status()
data = response.json()

df = pd.DataFrame(data["result_data"]["formList"])
print("원본 컬럼:", df.columns.tolist())

# 날짜 컬럼 처리
df["reg_date"] = df["date"].astype(str).str[:6]

# long 형식 변환
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
# 3. 인구 데이터 (총인구만)
# -------------------------
print("👥 인구 데이터 불러오는 중...")

pop_path = os.path.join(os.path.dirname(__file__), "population_total_filtered.csv")
pop_df = pd.read_csv(pop_path, encoding="utf-8")

print("✅ 인구 CSV 컬럼:", pop_df.columns.tolist())
print("✅ 인구 데이터:", len(pop_df), "rows")

# 월 확장 (연도 데이터를 12개월로 복제)
pop_df = pop_df.loc[pop_df.index.repeat(12)].copy()
pop_df["month"] = [i for i in range(1, 13)] * int(len(pop_df) / 12)
pop_df["reg_date"] = pop_df["year"].astype(str) + pop_df["month"].astype(str).str.zfill(2)

# -------------------------
# 4. 매칭 후 merge
# -------------------------
merged = pd.merge(
    veh_final,
    pop_df[["reg_date", "sido", "sigungu", "population"]],
    on=["reg_date", "sido", "sigungu"],
    how="inner"
)

merged["supply_rate"] = (merged["count"] / merged["population"]) * 1000
merged["period"] = merged["reg_date"]

print("✅ 보급률 계산 완료:", len(merged), "rows")
print(merged.head())

# -------------------------
# 5. DB 저장
# -------------------------
veh_final.to_sql("CAR_REGIST_SIDO", con=engine, if_exists="replace", index=False)
merged.to_sql("CAR_SUPPLY_RATE", con=engine, if_exists="replace", index=False)

print("✅ CAR_REGIST_SIDO 테이블 저장 완료")
print("✅ CAR_SUPPLY_RATE 테이블 저장 완료")
