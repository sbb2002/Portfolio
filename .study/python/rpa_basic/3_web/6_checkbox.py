# https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox')
browser.switch_to.frame('iframeResult')

# elem = browser.find_element_by_xpath('//*[@id="vehicle1"]')
# By를 import할 때:
# elem = browser.find_element(By.XPATH, '//*[@id="vehicle1"]')
elem = browser.find_element(By.ID, 'vehicle1')

# time.sleep(5)

if elem.is_selected() == False:
    print("선택합니다.")
    elem.click()
else:
    print("이미 선택되어있습니다.")

time.sleep(5)
browser.quit()