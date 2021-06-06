from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

chkvar = IntVar()   # chkbar에 int형으로 값을 저장
chkbox = Checkbutton(root, text="오늘 하루 보지않기", variable=chkvar)
# chkbox.select()     # 기본 선턱처리
# chkbox.deselect()   # 선택해제
chkbox.pack()

chkvar2 = IntVar()   # chkbar에 int형으로 값을 저장
chkbox2 = Checkbutton(root, text="일주일동안 보지않기", variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get())     # 0=해제, 1=체크
    print(chkvar2.get())     # 0=해제, 1=체크


btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()