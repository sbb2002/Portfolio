import pyperclip
import re
import csv_writer
import os, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome()
browser.get('https://www.kamis.or.kr/customer/price/retail/item.do?action=priceinfo&regday=2021-02-15&itemcategorycode=200&itemcode=211&kindcode=&productrankcode=&convert_kg_yn=N')

p = re.compile('[0-9]+')
p_kor = re.compile('[가-힣]+')

class elems:
    global browser

    def mth(self):
        browser.find_elements_by_xpath('//*[@id="regDatepicker"]/div/div/div/select[2]/*')
    
    def day(self):
        browser.find_elements_by_xpath('//*[@id="regDatepicker"]/div/table/tbody/*/*/a')

l_date = []
l_cost = []
data = []

start_year = 2021

while start_year >= 2011:
    a1 = elems()
    a2 = elems()
    
    a1.mth()
    for month in range(len(a1.mth())):
        a2.mth()
        mth_count = len(a1.mth()) - 1 - month
        mth = p.findall([ e.text for e in a2.mth() ][mth_count])[0]
        if int(mth) < 10:
            mth = "0" + mth
        a2.mth()[mth_count].click()
        browser.implicitly_wait(10)
        
        day_elems = browser.find_elements_by_xpath('//*[@id="regDatepicker"]/div/table/tbody/*/*/a')
        for num in range(len(day_elems)):
            inner_day_elems = browser.find_elements_by_xpath('//*[@id="regDatepicker"]/div/table/tbody/*/*/a')
            
            # date
            day = len(day_elems) - num
            date_day = str(day)
            if int(date_day) < 10:
                date_day = "0" + date_day
            date = str(start_year) + "-" + mth + "-" + date_day
            l_date.append(date)

            # move to cost_elem
            inner_day_elems[day - 1].click()  # 해당 일 클릭
            browser.find_element_by_xpath('//*[@id="ulitemcategorycode"]/li[2]/a').click()  # 배추
            browser.find_element_by_xpath('//*[@id="btn_search"]').click()  # 조회
            browser.implicitly_wait(10)
            
            # cost
            try:
                today_elem = p_kor.findall([ e.text for e in browser.find_elements_by_xpath('//*[@id="itemTable_1"]/tbody/tr[1]/th[2]') ][0])[0]
            
                if today_elem == "당일":
                    actions = ActionChains(browser)
                    cost_elem = browser.find_element_by_xpath('//*[@id="itemTable_1"]/tbody/tr[2]/td[2]')    # 가격
                    actions.double_click(on_element=cost_elem).perform()
                    actions.key_down(Keys.CONTROL).perform()
                    actions.key_down('c').perform()
                    actions.key_up(Keys.CONTROL).perform()
                    actions.key_up('c').perform()
                    result = p.findall(pyperclip.paste())
                    cost = int(result[0] + result[1])
                    l_cost.append(cost)
                    print("DATE: ", date, "\tCOST: ", cost)

                else:   # not allow the day outdated
                    l_cost.append("null")
                    print("DATE: ", date, "\tCOST: null")

            except: # 2017-10-09 ~ 2017-09-28: No data
                l_cost.append("null")
                print("DATE: ", date, "\tCOST: null")
                
            # left count
            print('This month session: {} left.\n'.format(day - 1))
        print("==================== {0}-{1} session over. ====================".format(start_year, mth))
    start_year -= 1
    inner_yr_elems = browser.find_elements_by_xpath('//*[@id="regDatepicker"]/div/div/div/select[1]/*') # 1~(11+n) ; n >= 1
    inner_yr_elems[9].click()

browser.quit()

print("==================== All of sessions are over. ====================")
print("Exporting csv file sequence is initiating.")

# csv exporting
for i in reversed(range(len(l_date))):
    data.append({'DATE':l_date[i], 'COST':l_cost[i]})
csv_writer.save_to_file(data)

time.sleep(5)

# system shutdown
if os.path.exists('cost_outputs.csv') == True:
    print("All of processing has been ended.\nSystem will be shuting down soon...")
    time.sleep(20)
    os.system('shutdown -s -t 10')