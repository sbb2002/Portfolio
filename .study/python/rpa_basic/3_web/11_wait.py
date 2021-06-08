# loading 시간 기다려주기

import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://flight.naver.com/flights/')

# 가는 날 클릭
browser.find_element_by_link_text('가는날 선택').click()
browser.find_elements_by_link_text('2')[1].click()

# 오는 날 클릭
browser.find_elements_by_link_text('23')[1].click()

# 주의!!!====================================================

# 가는날 선택 시, elem이 바뀌도록 되어있나보다.
# 따라서, 같은 날짜의 다음 달(ex. 1월 30일, 2월 30일)
# 을 선택할 때는 다음과 같이 써야한다.

# browser.find_elements_by_link_text('30')[0].click()
# browser.find_elements_by_link_text('30')[0].click()

# ===========================================================

# 제주도 클릭
browser.find_element_by_xpath('//*[@id="recommendationList"]/ul/li[1]').click()

# 항공권 검색 클릭
browser.find_element_by_link_text('항공권 검색').click()

# 1st 결과 출력 (로딩 대기)
# time.sleep(10)        
# but 타이트하게 동작하려면 다음과 같이 입력한다.
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    # 10초 동안 해당 XPATH가 출현할 때까지 대기, 나타나면 넘어감
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div/div[4]/ul/li[1]')))
    print(elem.text)
except:
    print("시간초과")

# elem = browser.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[4]/ul/li[1]')
# print(elem.text)

time.sleep(5)
browser.quit()


### 주의)
### find_element_~ = 단일 객체
### find_elements_~ = list[복수] 객체