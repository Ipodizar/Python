# vehicle_api.py
import pandas as pd
import requests
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

def fetch_vehicle_data(start_dt="201501", end_dt="202412", to_db=False, to_csv=False, csv_path="vehicle_data.csv"):
    """
    MOLIT API에서 차량 등록 데이터를 불러와 DataFrame 반환.
    필요시 DB 또는 CSV 파일로 저장할 수도 있음.
    """
    load_dotenv()
    engine = create_engine(
        f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
        f"@{os.getenv('DB_HOST')}:3306/{os.getenv('DB_NAME')}?charset=utf8mb4"
    )

    API_KEY = "4c49d1028d634c258ca4c7b99eb4a134"
    MOLIT_URL = "http://stat.molit.go.kr/portal/openapi/service/rest/getList.do"

    params = {
        "key": API_KEY,
        "form_id": 5498,
        "style_num": 2,
        "start_dt": start_dt,
        "end_dt": end_dt
    }

    response = requests.get(MOLIT_URL, params=params)
    response.raise_for_status()
    data = response.json()

    df = pd.DataFrame(data["result_data"]["formList"])
    df["reg_date"] = df["date"].astype(str).str[:6]

    value_cols = [c for c in df.columns if any(x in c for x in ["승용", "승합", "화물", "특수"])]

    long_df = df.melt(
        id_vars=["reg_date", "시도명", "시군구"],
        value_vars=value_cols,
        var_name="category",
        value_name="count"
    )

    long_df[["car_type", "usage_type"]] = long_df["category"].str.split(">", expand=True)

    final_df = long_df.rename(columns={
        "시도명": "sido",
        "시군구": "sigungu"
    })[["reg_date", "sido", "sigungu", "car_type", "usage_type", "count"]]

    final_df["count"] = pd.to_numeric(final_df["count"], errors="coerce").fillna(0).astype(int)

    final_df = final_df[
        (final_df["usage_type"] != "계") &
        (final_df["sigungu"] != "계") &
        (final_df["sido"] != "계")
    ].copy()

    if to_db:
        final_df.to_sql("CAR_REGIST_SIDO", con=engine, if_exists="append", index=False)
        print("✅ DB 적재 완료:", len(final_df), "rows")

    if to_csv:
        final_df.to_csv(csv_path, index=False, encoding="utf-8-sig")
        print(f"✅ CSV 저장 완료: {csv_path} ({len(final_df)} rows)")

    return final_df


# 실행 예시
if __name__ == "__main__":
    df = fetch_vehicle_data(start_dt="201501", end_dt="201512", to_csv=True, csv_path="vehicle_2015.csv")
    print(df.head())
