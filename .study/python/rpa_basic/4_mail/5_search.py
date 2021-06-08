from imap_tools import MailBox
from account import *

# mailbox = MailBox("imap.gmail.com")
# mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX")
# mailbox.logout()

# 더 간단하게
with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    # for msg in mailbox.fetch(limit=5, reverse=True):     # 전체메일 다 가져오기
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 읽지 않은 메일만 가져오기 (수신확인 처리됨)
    # for msg in mailbox.fetch('(UNSEEN)', limit=5, reverse=True):     # 전체메일 다 가져오기
        # print("[{}] {}".format(msg.from_, msg.subject))

    # 특정인이 보낸 메일만 가져오기
    # for msg in mailbox.fetch('(FROM sbb4113@gmail.com)', limit=5, reverse=True):
        # print("[{}] {}".format(msg.from_, msg.subject))

    # 어떤 글자가 제목이나 본문에 포함되는 메일 가져오기 (test, mail을 찾음)
    # for msg in mailbox.fetch('(TEXT "test mail")', limit=5, reverse=True):      #' " " ' 순서로 감쌀 것
        # print("[{}] {}".format(msg.from_, msg.subject))

    # 어떤 글자를 포함하는 메일, 제목만 보기
    # 한글은 에러가 나므로 유의. 다음 예시에서 우회법 설명.
    # for msg in mailbox.fetch('(SUBJECT "test mail")', limit=5, reverse=True):
        # print("[{}] {}".format(msg.from_, msg.subject))

    # 한글을 포함할 경우, if를 이용해 우회
    # for msg in mailbox.fetch(limit=5, reverse=True):
    #     if "테스트" in msg.subject:
    #         print("[{}] {}".format(msg.from_, msg.subject))
    
    # 특정 날짜 이후 메일만
    # for msg in mailbox.fetch('(SENTSINCE 07-Nov-2020)', limit=5, reverse=True):
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 특정 날짜에 온 메일만
    # for msg in mailbox.fetch('(ON 07-Nov-2020)', limit=5, reverse=True):
        # print("[{}] {}".format(msg.from_, msg.subject))

    # 2가지 조건 이상을 모두 만족하는 메일
    #  for msg in mailbox.fetch('(SENTSINCE 07-Nov-2020 SUBJECT "test mail")', limit=5, reverse=True):
        # print("[{}] {}".format(msg.from_, msg.subject))

    # 여러 조건 중 하나라도 만족하는 메일
     for msg in mailbox.fetch('(OR SENTSINCE 07-Nov-2020 SUBJECT "test mail")', limit=5, reverse=True):
        print("[{}] {}".format(msg.from_, msg.subject))



### REF)
# 메일 조건 쿼리:
# https://pypi.org/project/imap-tools/