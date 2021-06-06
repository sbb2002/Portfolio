# [신청 메일 양식]
# 제목: 파이썬 특강 신청합니다.
# 본문: 닉네임 / 전화번호 뒤 4자리
    # ex) 나도코딩 / 1234

from imap_tools import MailBox
from account import *

applicant_list = []

with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    index = 1 # 순번
    for msg in mailbox.fetch('(SENTSINCE 31-Jan-2021)'):
        if "파이썬 특강" in msg.subject:
            nickname, phone = msg.text.strip().split("/")   # strip을 넣으면 암묵적인 \n를 떼준다.
            print("순번: {} 닉네임: {} 전화번호: {}".format(index, nickname, phone))
            applicant_list.append((msg, index, nickname, phone))
            index += 1

for applicant in applicant_list:
    print(applicant)    # tuple로 저장