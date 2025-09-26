# 01_population_transport.py
import pandas as pd

def load_population_data(pop_file: str) -> pd.DataFrame:
    """인구 데이터 정제"""
    pop_df = pd.read_csv(pop_file, encoding="euc-kr")
    pop_df = pop_df[~pop_df["행정구역별(읍면동)"].isin(["전국", "읍부", "면부", "동부"])]
    population_df = pop_df[["행정구역별(읍면동)", "2023"]].rename(columns={
        "행정구역별(읍면동)": "region_name",
        "2023": "population"
    })
    population_df["population"] = pd.to_numeric(population_df["population"], errors="coerce")
    return population_df


def load_transit_data(transit_file: str) -> pd.DataFrame:
    """대중교통 데이터 정제 및 1인당 주간 이용 횟수 계산"""
    transit_df = pd.read_csv(transit_file, encoding="euc-kr")
    transit_df = transit_df[transit_df["구분(1)"] != "전체"]

    percent_cols = ["2023.2", "2023.3", "2023.4", "2023.5", "2023.6"]
    for col in percent_cols:
        transit_df[col] = pd.to_numeric(transit_df[col], errors="coerce")

    bins = {
        "2023.2": 4.5,
        "2023.3": 8,
        "2023.4": 13,
        "2023.5": 18,
        "2023.6": 21
    }

    def weighted_avg(row):
        total = 0
        for col, weight in bins.items():
            if pd.notna(row[col]):
                total += row[col] * weight / 100
        return total

    transit_df["weekly_transit_per_capita"] = transit_df.apply(weighted_avg, axis=1)
    transit_df = transit_df[["구분(1)", "weekly_transit_per_capita"]].rename(columns={
        "구분(1)": "region_name"
    })
    return transit_df


# 이 파일을 직접 실행했을 때만 동작하도록
if __name__ == "__main__":
    BASE_DIR = "/Users/joonseok/Desktop/AI/SKN20_1st_2Team"
    pop_file = f"{BASE_DIR}/population_2023.csv"
    transit_file = f"{BASE_DIR}/transportation_2023.csv"

    pop_df = load_population_data(pop_file)
    transit_df = load_transit_data(transit_file)

    print("인구 데이터 미리보기:\n", pop_df.head())
    print("\n대중교통 데이터 미리보기:\n", transit_df.head())
