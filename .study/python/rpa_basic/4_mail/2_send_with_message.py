import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일입니다."   # 제목
msg["from"] = EMAIL_ADDRESS            # 보낸 이
msg["To"] = "sbb4113@gmail.com"        # 받는 이

# 여러 명에게 메일을 보낼 때
# 1) msg["To"] = "sbb4113@gmail.com, sbb2005@naver.com"
# 2) to_list = ["sbb4113@gmail.com", "sbb2005@naver.com"]
#    msg["To"] = ", ".join(to_list)      # to_list의 list를 ", "로 구분하여 합침

# 참조
# msg["Cc"] = "sbb4113@gmail.com"

# 비밀참조
# msg["Bcc"] = "sbb4113@gmail.com"

msg.set_content("테스트 본문입니다.")   # 본문

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

### 1_send.py 와 달리 한글 텍스트 인코딩 에러가 발생하지 않는다.