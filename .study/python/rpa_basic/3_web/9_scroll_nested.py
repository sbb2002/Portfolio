# https://www.w3schools.com/html/

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/html/')
browser.maximize_window()
time.sleep(5)

# 특정 영역 스크롤
elem = browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[61]')

# 1) ActionChain
# actions = ActionChains(browser)
# actions.move_to_element(elem).perform()

# 2) 좌표대입
# xy = elem.location_once_scrolled_into_view      # 좌표정보함수; ()안씀
# print("type: ", type(xy))
# print("type: ", xy)

elem.click()        # 스크롤 이동 안해도 클릭은 잘 수행함

time.sleep(5)
browser.quit()