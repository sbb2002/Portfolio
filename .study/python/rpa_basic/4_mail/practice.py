# 메일 날짜 찾을 떄 활용
import time
print(time.strftime('%d-%b-%Y-%a'))    # 현재 날짜 일-월-연도-요일

import datetime
dt = datetime.datetime.strptime("2020-12-30", "%Y-%m-%d")   # 사람에게 친숙한 날짜 --> 컴퓨터 문법 날짜
print(type(dt))
print(dt.strftime('%d-%b-%Y'))