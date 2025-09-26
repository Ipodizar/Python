import requests
import pandas as pd

# API 요청 URL
url = "http://stat.molit.go.kr/portal/openapi/service/rest/getList.do"
params = {
    "key": "4c49d1028d634c258ca4c7b99eb4a134",  # 인증키
    "form_id": 5559,   # 이륜차신고현황 시도별
    "style_num": 1,
    "start_dt": 202508,
    "end_dt": 202508
}

# API 호출
response = requests.get(url, params=params)

# JSON 응답 → dict
data = response.json()

# formList 부분만 꺼내기
form_list = data["result_data"]["formList"]

# DataFrame 변환
df = pd.DataFrame(form_list)

# 가독성 좋게 출력 (상위 5개만 예시)
print(df.head())

# Jupyter 환경이라면 표 형태로 바로 확인 가능
df
