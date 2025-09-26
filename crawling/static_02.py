import requests
# 데이터를 요청할 주소
url = 'https://www.hollys.co.kr/store/korea/korStore2.do?'
# 서버에 보낼 데이터 (1페이지를 보여달라는 의미로)
from_data = {
    'pageNo' : 1,
    'sido' : '',
    'gugun' : '',
    'store' : ''
}
response = requests.post(url, data = from_data)

# 터미널에서 pip install beautifulsoup4 실행
from bs4 import BeautifulSoup
# response에 있는 문자열로 된 데이터를 BeautifulSoup 객체로 변환 --> 첫 글자 대문자 : 클래스
soup = BeautifulSoup(response.text, 'html.parser')

# 원하는 정보를 추출 --> 원하는 위치를 찾아야함 
# -->fn+f12 개발자도구 진입, Inspect 누르고 원하는 거 웹페이지에서 누르기 --> copy selector
#contents > div.content > fieldset > fieldset > div.tableType01 > table > tbody > tr
str_table_rows = '#contents > div.content > fieldset > fieldset > div.tableType01 > table > tbody > tr '
# soup.select('tbody > tr') tbody가 한 개 밖에 없어서 가능. 만약 여러개면 가장 먼저 만나는 tbody
#contents > div.content > fieldset > fieldset > div.tableType01 > table > tbody > tr:nth-child(1)
store_rows = soup.select(str_table_rows)
store_lists=[]
for row in store_rows:
    store_lists.append(
    (
    row.select('td')[0].text.strip(),  # td 하나씩 다 찾아줌, .text는 태그 제외하고 텍스트만 출력 --> 지역
    row.select('td')[1].text.strip(),  # 매장명
    row.select('td')[2].text.strip(),  # 현황
    row.select('td')[3].text.strip(),  # 주소
    row.select('td')[5].text.strip()  # 전화번호
    )
    )
 
print(store_lists)


