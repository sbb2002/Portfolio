# Selenium 을 이용해 자동 업무수행 프로그램을 작성하시오.
# 1. w3schools.com에 접속
# 2. Learn html > how to > contact form
# 3. 세 입력란에 다음과 같이 적으시오.
    # -First name: 나도
    # -Last name: 코딩
    # -Country: Canada
    # -Subject: 퀴즈 완료하였습니다.
    # 위 값들은 변수로 미리 저장해둘 것.
# 4. 5초 대기 후 Submit 클릭
# 5. 5초 대기 후 브라우저 종료

import time
import pyautogui
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def kor_text(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl","v")

first_name = "나도"
last_name = "코딩"
country = "Canada"
subject_text = "퀴즈를 완료하였습니다."

browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/')
browser.maximize_window()

browser.find_element_by_xpath('//*[@id="mySidenav"]/div/a[1]').click()
browser.find_element_by_xpath('//*[@id="topnav"]/div/div[1]/a[10]').click()
browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[116]').click()

# browser.find_element_by_link_text('Contact Form').click()
# browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[text()="Contact Form"]').click()
# browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[contains(text(), "Contact")]').click()

### 이 세 줄은 그 위의 줄과 동일함.
### 1번: link_text로 직접적으로 찾기. 오타 및 대소문자에 매우 주의!
### 2번: xpath를 활용, Contact Form이라는 글자만 찾아서 동작.
###3번: xpath를 활용, Contact 글자가 포함된 것을 찾아 동작.

browser.find_element_by_xpath('//*[@id="fname"]').click()
kor_text(first_name)
browser.find_element_by_xpath('//*[@id="lname"]').send_keys(last_name)
browser.find_element_by_xpath('//*[@id="country"]/option[text()="{}"]'.format(country)).click()
browser.find_element_by_xpath('//*[@id="main"]/div[3]/textarea').send_keys(subject_text)

time.sleep(5)
browser.find_element_by_xpath('//*[@id="main"]/div[3]/a').click()

time.sleep(5)
browser.quit()