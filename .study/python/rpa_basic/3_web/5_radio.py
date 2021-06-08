# Radio_btn = 옵션으로 단 1개만 선택하는 버튼
import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()       # 창 최대화
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')
browser.switch_to.frame('iframeResult')
elem = browser.find_element_by_xpath('//*[@id="male"]')

# 선택 안되었으면 선택하기
if elem.is_selected() == False:
    print('선택안되었네용? 눌렀읍니다..')
    elem.click()
else:
    print('선택되어있어서 가만히 있읍니다')

time.sleep(5)

if elem.is_selected() == False:
    print('선택안되었네용? 눌렀읍니다..')
    elem.click()
else:
    print('선택되어있어서 가만히 있읍니다')

browser.quit()

# =============================================================
# 실행 중에 마우스 까닥까닥하면 오만가지 에러가 뜬다.
# 그닥 큰 영향은 없으나 신경쓰이므로
# 실행 중에는 종료까지 건들지 말자.
# =============================================================
