import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

# 기차 예매 시스템 가정
def info():
    msgbox.showinfo("알림", "정상적으로 예매되었습니다.")

def warn():
    msgbox.showwarning("경고", "이미 예매된 좌석입니다.")

def error():
    msgbox.showerror("에러", "결제 오류가 발생했습니다.")

def okcancel():
    msgbox.askokcancel("확인 / 취소", "해당 좌석은 유아동반석입니다. 그래도 예매하시겠습니까?")

def retrycancel():
    response = msgbox.askretrycancel("재시도 / 취소", "일시적인 오류입니다. 다시 시도하시겠습니까?")
    if response == 1:
        print("재시도")
    elif response == 0:
        print("취소")

def yesno():
    response = msgbox.askyesno("예/ 아니오", "해당 좌석은 역방향입니다. 그래도 예매하시겠습니까?")
    print(response)

def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="예매 내역이 저장되지 않았습니다.\n저장 후 종료하시겠습니까?")
    # 네: 저장 후 종료
    # 아니오: 저장 안하고 종료
    # 취소: 프로그램 종료취소 (현재화면에서 계속 작업)
    print("응답: ", response)   # T/F/None = 1/0/else
    if response == 1:
        print("예")
    elif response == 0:
        print("아니오")
    else:
        print("취소")

def askquestion():
    response = msgbox.askquestion("질문", "확실합니까?")
    print(response)
    if response == 1:
        print("확실")
    elif response == 0:
        print("아니")

Button(root, command=info, text="예매").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()
Button(root, command=okcancel, text="확인 취소").pack()
Button(root, command=retrycancel, text="재시도 취소").pack()
Button(root, command=yesno, text="예 아니오").pack()
Button(root, command=yesnocancel, text="예 아니오 취소").pack()
Button(root, command=askquestion, text="확실 아니").pack()




root.mainloop()