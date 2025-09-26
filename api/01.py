from dotenv import load_dotenv
import os
import requests
# .env 로드
load_dotenv()
P_KEY = os.getenv('PUBLIC_KEY')
print(f'P_KEY : {P_KEY[:10]}')
url = 'https://www.data.go.kr/data/15059401/openapi.do#/API%20%EB%AA%A9%EB%A1%9D/getnewRegistlnfoService'
# 물음표가 있어야 연결됨
# 서버에 보낼 데이터 (1페이지를 보여달라는 의미로)
from_data = {
    'serviceKey' : P_KEY,
    'registYy' : '2024',
    'registMt' : '12',
    'vhctyAsortCode' : '2',
    'registGrcCode' : '1',
    'useFuelCode' : '6'
}
response = requests.get(url, data = from_data)
print(response.text[:500])