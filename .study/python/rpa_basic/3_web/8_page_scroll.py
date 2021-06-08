import time
from selenium import  webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.maximize_window()

browser.get('https://shopping.naver.com/')

# 무선마우스 입력
# browser.find_element_by_xpath('//*[@id="autocompleteWrapper"]/input[1]').send_keys("무선마우스")

# 검색버튼 클릭
# browser.find_element_by_xpath('//*[@id="autocompleteWrapper"]/a[2]').click()

# 안되면 풀어써보자
elem = browser.find_element_by_xpath('//*[@id="autocompleteWrapper"]/input[1]')
elem.send_keys("무선마우스")

time.sleep(5)
elem.send_keys(Keys.ENTER)

# 스크롤 =====================================================

# 1) 지정한 위치로 스크롤 내리기
# browser.execute_script('window.scrollTo(0, 1080)')   # 모니터 세로크기 1080px 만큼 내림 = 1page 내려감

# 2) 화면을 현재 기준으로 가장 밑으로 내리기 (end 누른 효과)
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

# 3) 동적 페이지에 대해서 마지막까지 스크롤 반복 수행
interval = 2        # 2초에 한번씩
prev_height= browser.execute_script('return document.body.scrollHeight')
while True:
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(interval)        # 너무 빠르면 못따라가기 때문
    curr_Height = browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    if curr_Height == prev_height:
        break
    prev_height = curr_Height       # prev를 curr로 업데이트

# 4) 맨 위로 올리기
browser.execute_script('window.scrollTo(0, 0)')
# ============================================================

time.sleep(5)
browser.quit()