# merge_indicators.py
import pandas as pd
from population_transport import load_population_data, load_transit_data
from vehicle_api import fetch_vehicle_data
import os
from dotenv import load_dotenv
from db_utils import get_engine, save_dataframe   # ✅ 이 줄 중요!

# .env 불러오기 (최초 1회만)
load_dotenv()

# 시도명 정규화 매핑
REGION_MAP = {
    "서울": "서울특별시", "부산": "부산광역시", "대구": "대구광역시", "인천": "인천광역시",
    "광주": "광주광역시", "대전": "대전광역시", "울산": "울산광역시", "세종": "세종특별자치시",
    "경기": "경기도", "강원": "강원특별자치도", "충북": "충청북도", "충남": "충청남도",
    "전북": "전북특별자치도", "전남": "전라남도", "경북": "경상북도", "경남": "경상남도",
    "제주": "제주특별자치도"
}

def normalize_region(df: pd.DataFrame, col: str = "region_name") -> pd.DataFrame:
    df[col] = df[col].replace(REGION_MAP)
    return df

def merge_indicators(pop_file: str, transit_file: str, start_month: int = 202301, end_month: int = 202312) -> pd.DataFrame:
    population_df = load_population_data(pop_file)
    transit_df = load_transit_data(transit_file)
    vehicle_df = fetch_vehicle_data(start_month, end_month)

    # 🚀 월별·시도별 합계
    vehicle_df = vehicle_df.groupby(["stat_ym", "region_name"], as_index=False)["vehicle_total"].sum()

    # 시도명 정규화
    population_df = normalize_region(population_df, "region_name")
    transit_df = normalize_region(transit_df, "region_name")
    vehicle_df = normalize_region(vehicle_df, "region_name")

    # 인구 + 대중교통 병합
    base_df = pd.merge(population_df, transit_df, on="region_name", how="inner")

    # 자동차 등록대수와 병합
    final_df = pd.merge(vehicle_df, base_df, on="region_name", how="inner")

    # 천명당 자동차 보급률 계산
    final_df["vehicles_per_1000"] = (final_df["vehicle_total"] / final_df["population"]) * 1000
    return final_df

if __name__ == "__main__":
    BASE_DIR = "/Users/joonseok/Desktop/AI/SKN20_1st_2Team"
    pop_file = f"{BASE_DIR}/population_2023.csv"
    transit_file = f"{BASE_DIR}/transportation_2023.csv"

    result_df = merge_indicators(pop_file, transit_file, 202301, 202312)
    print("최종 데이터 미리보기:")
    print(result_df.head())

    # ✅ MySQL 저장
    engine = get_engine()
    save_dataframe(result_df, "fact_vehicle_stats", engine, if_exists="replace")
