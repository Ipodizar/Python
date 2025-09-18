# pip install pymysql  # mysql을 접속할 수 있는 라이브러리
# pip install dotenv  # 환경변수 .env를 로드할 수 있는 라이브러리
import pymysql
from dotenv import load_dotenv
import os

# .env 로드
load_dotenv()

# 1. DB 연결
conn = pymysql.connect(
    host = os.getenv('DB_HOST'),
    user = os.getenv('DB_USER'),
    password = os.getenv('DB_PASSWORD'),
    database = os.getenv('DB_NAME')
)
print('접속성공')

# 2. 각 테이블별
    # C - insert
    # R - select
    # U - update
    # D - delete
#  고객 - customer
def create_customer(name):
    sql = 'insert into customer values(null, %s)'
    cur = conn.cursor()
    cur.execute(sql, '이순신')
    conn.commit()
    print('고객추가 완료')

sql = 'select * from customer'
cur = conn.cursor()
cur.execute(sql)
# 3. 메소드
    # 회원가입
    # 상품정보 출력
    # 상품구입
    # 상품정보 입력
    # 대쉬보드 : 고객별 상품별 구매횟수, 평균 구매액
# 4. 기능 구현과 테스트가 되면.. streamlit으로 UI 구성 - 템플릿 화면을 보고 유사한 형태로 구현

conn.close() # 접속해제