# https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio
# //*[@id="male"]

import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')
browser.switch_to.frame('iframeResult')
elem = browser.find_element_by_xpath('//*[@id="male"]')     # 위 문장없이 작동 x -> iframe정의해줘야함
elem.click()
# browser.switch_to_default_content()       # 상위로 이동
time.sleep(5)

browser.quit()