#pypi - beautifulsoup4
# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())

# 내장 함수
# dir : import로 갖고 온 것 중에 사용가능한 함수 알려줌
# print(dir())
# import random
# print(dir())
# import pickle
# print(dir(random))

# lst = [1,2,3]
# print(dir(lst))

# name = "Jim"
# print(dir(name))

# 외장 함수 : import 해서 갖고옴
# glob
# import glob
# print(glob.glob("*.py"))    # 파일 찾기

# os
import os
# print(os.getcwd())      # 경로 찾기
#
# folder = "sample_dir"
#
# if os.path.exists(folder):
#     print("이미 있는 폴더입네다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 내래 숙청했디.")
# else:
#     os.makedirs(folder)
#     print(folder,"폴더 생성됨")

# print(os.listdir())     # glob

# time
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %h:%M:%S"))
import datetime
# print("오늘 날짜는 ", datetime.date.today())

#timedelta : 날짜 간격
today = datetime.date.today()
td = datetime.timedelta(days=100)
print("우리가 만난지 100일은", today + td)