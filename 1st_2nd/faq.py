import requests
import html
from bs4 import BeautifulSoup

url = "https://www.hyundai.com/wsvc/front/biz/frontFaq.faqListArr.do"

headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "origin": "https://www.hyundai.com",
    "referer": "https://www.hyundai.com/kr/ko/faq.html",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
}

cookies = {
    "HJSESSIONID": "node01bh930pgz1heew3ozw9b6m6id487525.node0",
    "JSESSIONID": "node01bh930pgz1heew3ozw9b6m6id487525-org.apache.sling",
}

faq_list = []
page = 1

while True:
    payload = {
        "searchKeyword": "",
        "pageNo": str(page),
        "frontSupiCtgr": "",
        "frontCtgrScd": "",
    }

    res = requests.post(url, headers=headers, cookies=cookies, data=payload)
    data = res.json()

    items = data.get("data", [])
    if not items:
        break

    for item in items:
        category = item["frontSupiCtgrNM"].strip()
        question = item["frontFaqTitlSbc"].strip()

        # HTML 파싱 후 모든 텍스트 합치기
        raw_html = html.unescape(item["frontFaqSbc"])
        soup = BeautifulSoup(raw_html, "html.parser")
        answer = soup.get_text(separator="\n").strip()

        faq_list.append((category, question, answer))

    print(f"✅ Page {page} 수집: {len(items)}건")
    page += 1

print("총 FAQ 개수:", len(faq_list))

# 일부 출력 확인
for row in faq_list[:3]:
    print("카테고리:", row[0])
    print("질문:", row[1])
    print("답변:", row[2])
    print("-" * 50)

# ======================
# 2. DB 저장 코드 (이 부분 새로 붙이기)
# ======================
import pymysql
import os
from dotenv import load_dotenv

# .env 불러오기
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

# MySQL 연결
conn = pymysql.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME,
    charset="utf8mb4"
)

cursor = conn.cursor()

# ⚠️ 테이블명을 FAQ 로 지정
sql = """
INSERT INTO FAQ (category, question, answer)
VALUES (%s, %s, %s)
"""

# faq_list 변수를 그대로 사용
cursor.executemany(sql, faq_list)
conn.commit()

print(f"✅ {cursor.rowcount}건 삽입 완료")

cursor.close()
conn.close()