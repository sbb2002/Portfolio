from imap_tools import MailBox
from account import *
import re

mailbox = MailBox("imap.gmail.com", 993)
mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX")

# limit = 최대메일갯수, reverse=T(최근부터)/T(과거부터)
for msg in mailbox.fetch(limit=1, reverse=True):
    print("제목", msg.subject)
    print("발신자", msg.from_)
    print("수신자", msg.to)
    # print("참조자", msg.cc)
    # print("비밀참조자", msg.bcc)
    print("날짜", msg.date)     #GMT-8 출력; 한국 GMT+9 => 17h차이
    print("본문", msg.text)
    print("HTML 메시지", msg.html)
    print("=" * 88)

    # 첨부파일
    for att in msg.attachments:
        print("첨부파일 이름", att.filename)
        print("타입", att.content_type)
        print("크기", att.size)

        # ==========================================================
        # 하필 이때 파일이름이 경로명하고 비슷해서 그런지 경로로 인식함
        # 메일의 첨부파일 이름을 수정하라고 요청할 수도 있겠으나...
        # 혹은 너무 많다던가 해서 그럴 여건이 안된다면???????

        # 그러면 정규표현식을 이용하여 [파일명.확장자] 꼴로 
        # filename을 새로 정의하자.

        # import re
        p = re.compile('[a-zA-Z0-9_가-힣]+')
        result = p.findall(att.filename)
        l = []
        for l_count in range(1, len(p.findall(att.filename))):
            if l_count == len(p.findall(att.filename))-1:
                l.append(result[l_count])
            elif l_count == len(p.findall(att.filename))-2:
                l.append(result[l_count])
        f_name = l[0] + "." + l[1]
        # ==========================================================

        #다운로드
        with open('download_' + f_name, "wb") as f:
            f.write(att.payload)
            print("첨부파일 {} 다운로드 완료\n".format('download_' + f_name))
    print("=" * 88)


mailbox.logout()