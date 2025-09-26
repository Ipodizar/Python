import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from db_utils import get_engine
from dotenv import load_dotenv
import os

# .env 불러오기 (같은 폴더라면 경로 지정 필요 없음)
load_dotenv()

print("DEBUG STREAMLIT:", os.getenv("DB_HOST"), os.getenv("DB_USER"), os.getenv("DB_NAME"))

# ✅ 한글 폰트 설정 (macOS: AppleGothic, Windows: Malgun Gothic, Linux: NanumGothic)
plt.rcParams["font.family"] = "AppleGothic"
plt.rcParams["axes.unicode_minus"] = False  # 마이너스 기호 깨짐 방지

st.set_page_config(page_title="Mobility Dashboard", layout="wide")
st.title("🚍 대중교통 이용률 vs 🚗 차량 보급률 분석 대시보드")

# DB 연결
engine = get_engine()

# 데이터 불러오기
@st.cache_data
def load_data():
    query = """
        SELECT region_name, stat_ym, vehicles_per_1000, weekly_transit_per_capita
        FROM fact_vehicle_stats
    """
    df = pd.read_sql(query, engine)
    return df

df = load_data()

# 지역 선택 필터
regions = st.multiselect(
    "지역을 선택하세요:",
    options=df["region_name"].unique(),
    default=["서울특별시", "경기도", "부산광역시"]
)

filtered_df = df[df["region_name"].isin(regions)]

# 📊 산점도 (보급률 vs 대중교통 이용률)
st.subheader("산점도: 대중교통 이용률과 차량 보급률 관계")
fig, ax = plt.subplots()
ax.scatter(
    filtered_df["vehicles_per_1000"],
    filtered_df["weekly_transit_per_capita"],
    alpha=0.7
)
ax.set_xlabel("천명당 차량 보급률")
ax.set_ylabel("주간 1인당 대중교통 이용률")
ax.set_title("대중교통 vs 차량 보급률 (선택 지역)")
st.pyplot(fig)

# 📈 월별 추이 (라인차트)
st.subheader("월별 추이 비교")
for region in regions:
    region_df = filtered_df[filtered_df["region_name"] == region].sort_values("stat_ym")
    st.line_chart(
        region_df.set_index("stat_ym")[["vehicles_per_1000", "weekly_transit_per_capita"]],
        height=300,
        use_container_width=True
    )

# 📊 지역별 평균값 테이블
st.subheader("지역별 평균값 비교")
avg_df = (
    filtered_df.groupby("region_name", as_index=False)[["vehicles_per_1000", "weekly_transit_per_capita"]].mean()
    .round(2)
)
st.dataframe(avg_df)
