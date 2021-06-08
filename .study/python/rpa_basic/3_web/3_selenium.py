# chrome://version/
# 크롬 드라이브 이용 시, 위에서 버전확인 필수
# pip install selenium


from selenium import webdriver

# browser = webdriver.Chrome(r".\\rpa_basic\\3_web\\chromedriver_win32\\chromedriver.exe")
browser = webdriver.Chrome()        # 같은 위치에 있을 때
browser.get("http://daum.net")
browser.find_element_by_xpath('//*[@id="daumSearch"]/fieldset/div/div/button[2]')

### BUT!!
### 에디터에서 실행하면 실행할 때마다 크롬이 중복해서 켜지므로
### 실시간 응답을 목적으로 하면 터미널을 이용해서 할 것!!! (개빡침)


# =============================================================
# webdriver.Chrome( chromedriver.exe의 위치??? )
# import fnmatch, os
# pattern = "chromedriver.exe"
# result = []
# for root, dirs, files in os.walk("."):
#     for name in files:
#         if fnmatch.fnmatch(name, pattern):
#             result.append(os.path.join(root, name))
# print(result)
# =============================================================


# 참고!!
# 1) selenium 자습서
# https://selenium-python.readthedocs.io/locating-elements.html
# 2) 소스코드
# https://nadocoding.tistory.com/15
