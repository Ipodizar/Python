# pip install selenium webdriver-manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common. by import By
from selenium.webdriver.common. keys import Keys # return키 등을 입력하기 위해서
import time

# 웹 드라이버를 자동으로 설치하고 최신버전을 유지
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://www.google.com/')
print('브라우져가 성공적으로 열렸습니다.')

# 검색창 요소 찾기 (id가 'ipt_keyword_recruit'인 input 태그를 찾음)
search_input = driver.find_element(By.CLASS_NAME, 'gLFyf')
# 검색창에 파이썬 입력
search_input.send_keys('파이썬')
# return키 누르기
search_input.send_keys(Keys.RETURN)
time.sleep(3) # 대략 3초정도 페이지 로드 될 때까지 기다림

# 종료방지
input("브라우저를 닫으려면 엔터를 누르세요...")
# driver.quit()


