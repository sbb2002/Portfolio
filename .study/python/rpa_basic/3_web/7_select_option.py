import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_option')
browser.switch_to_frame("iframeResult")

# //*[@id="cars"]/option[4]

# cars에 해당하는 elemet를 찾고, 드롭다운 내부에 있는 4번째 옵션선택
# elem = browser.find_element_by_xpath('//*[@id="cars"]/option[4]')
# elem.click()

# 텍스트 값을 통해서 선택하는 방법(단, 완전 동일해야함); 위와 동일
# elem = browser.find_element_by_xpath('//*[@id="cars"]/option[text()="Audi"]')
# elem.click()

# 텍스트 값이 부분일치하는 항목선택 (Au가 들어가는 항목)
elem = browser.find_element_by_xpath('//*[@id="cars"]/option[contains(text(), "Au")]')
elem.click()


time.sleep(5)
browser.quit()