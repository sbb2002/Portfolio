import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://www.w3schools.com/tags/att_input_type_radio.asp')

curr_handle = browser.current_window_handle
print(curr_handle)

# Try it yourself 버튼
browser.find_element_by_xpath('//*[@id="main"]/div[2]/a').click()
# 이제 브라우저가 2탭이 켜짐

handles = browser.window_handles    # 모든 핸들 정보
for handle in handles:
    print("\n", handle)
    browser.switch_to.window(handle)    # 각 핸들로 이동
    print(browser.title)        # 브라우저 이름 표시
    print()

### 새로 이동된 브라우저에서 자동화 작업을 수행... ###

# 새 핸들 종료
print("현재 핸들을 종료합니다.\n")
browser.close()

# 이전 핸들로 이동
print("처음 핸들로 돌아갑니다.")
browser.switch_to.window(curr_handle)

print(browser.title) # HTML input type="radio"

# 브라우저 컨트롤이 되는지 확인하기
time.sleep(5)
browser.get('http://daum.net')

time.sleep(5)
browser.quit()