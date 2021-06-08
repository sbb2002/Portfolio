import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일입니다."
msg["from"] = EMAIL_ADDRESS
msg["To"] = "sbb4113@gmail.com"
msg.set_content("다운로드하세요")   # 본문

# msg.add_attachment(path)
    # 파일 path는 file을 우클릭해서 copy path를 선택하면 간단하다.
    # 1) Relative path: rpa_basic\2_desktop\play.png
    # 2) All path: C:\Users\J\Desktop\untitled\rpa_basic\2_desktop\play.png
    # with open을 이용해서도 할 수 있다.

# workspace = untitled이기에 경로를 지정해서 넣어줘야 한다.
# 다만, 이러면 첨부파일 이름도 경로가 삽입된다.
# 다음 챕터에서 피를 봤다. 다음부터...
# 파일 관리할 때는 workspace에 위치시키면 많이 편리해질 것 같다...

with open("./rpa_basic/2_desktop/play.png", "rb") as f:
    msg.add_attachment(f.read(), maintype="image", subtype="png", filename=f.name)
    
    # MINE TYPE: 미디어 종류를 구분
    # maintype과 subtype은 MINE type을 따라간다. main / sub
    # 파일 타입을 MINE type에 맞춰 기재하되,
    # 잘 모르겠거나 임의의 타입이라면 다음같이 기술한다.
    # *.txt --> text / plain
    # *.*   --> application / octet-stream (거침없이 열어버리므로 보안에 유의)
    # 자세한 것은 REF)참조

with open(r".\rpa_basic\4_mail\테스트.pdf", "rb") as f:
    msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename=f.name)

with open(r"rpa_basic\4_mail\테스트.xlsx", "rb") as f:
    msg.add_attachment(f.read(), maintype="application", subtype="octet-stream", filename=f.name)

# 현재까지 3개 파일이 업로드됨.

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)



### REF)
# MINE type:
# https://developer.mozilla.org/ko/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types
