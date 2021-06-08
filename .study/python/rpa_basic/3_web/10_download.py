# https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option('prefs', {'download.default_directory':r'C:\Users\J\Desktop\untitled'})

# options를 입력해주면 원하는 경로로 다운로딩
browser = webdriver.Chrome(options=chrome_options)
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download')

browser.switch_to.frame('iframeResult')

elem = browser.find_element_by_xpath('/html/body/p[2]/a')
elem.click()        # options로 경로지정 안하면 다운로드 폴더로 다운로딩

time.sleep(5)
browser.quit()