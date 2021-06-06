import pyperclip
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome()
browser.get('https://www.kamis.or.kr/customer/price/retail/item.do?action=priceinfo&regday=2021-02-15&itemcategorycode=200&itemcode=211&kindcode=&productrankcode=&convert_kg_yn=N')

p = re.compile('[가-힣]+')

today_elem = p.findall([ e.text for e in browser.find_elements_by_xpath('//*[@id="itemTable_1"]/tbody/tr[1]/th[2]') ][0])[0]
print(today_elem)
print(type(today_elem))


print(type(browser.find_element_by_xpath('//*[@id="itemTable_1"]/tbody/tr[1]/th[2]')))
print(type(browser.find_elements_by_xpath('//*[@id="itemTable_1"]/tbody/tr[1]/th[2]')))