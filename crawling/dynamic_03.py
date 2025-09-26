from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # enter키 등을 입력하기위해서
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup
import time

url = 'https://auto.danawa.com/auto/?Work=record'
#웹 드라이버를 자동으로 설치하고 최신버전을 유지
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 사이트 접속
driver.get(url)
# driver.maximize_window() # 전체 화면으로 실행  옵션
print('사이트 접속했습니다.')
# 사이트가 로드될때까지 기다린다.
time.sleep(1)
radio = driver.find_element(By.CSS_SELECTOR, "input[name = 'rdoMonthPeriod'][value = 'period']") # 그냥 디버깅에 뜨는 거 복붙하면 됨
radio.click()
time.sleep(1)

select= Select(driver.find_element(By.ID,'selMonthFrom'))
select.select_by_value('2023')
time.sleep(1)

select= Select(driver.find_element(By.ID,'selDayFrom'))
select.select_by_value('01')
time.sleep(1)

select= Select(driver.find_element(By.ID,'selMonthTo'))
select.select_by_value('2023')
time.sleep(1)

select= Select(driver.find_element(By.ID,'selDayTo'))
select.select_by_value('12')
time.sleep(2)

search_btn = driver.find_element(By.CSS_SELECTOR, "input[value='조회']") 
search_btn.click()
time.sleep(2)

more_btn = driver.find_element(By.CSS_SELECTOR,"#autodanawa_gridC > div.gridMain > article > main > div > div:nth-child(4) > div.left > a")
more_btn.click()    



time.sleep(9)
# 브라우져 종료
driver.quit()
print('접속 종료')