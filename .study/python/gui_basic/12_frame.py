
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

Label(root, text="메뉴를 선택해주세요.").pack(side="top")

Button(root, text="주문하기").pack(side="bottom")

# 버거킹
# 1. 버거
frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side="left", fill="both", expand=True)

Button(frame_burger, text="콰트로치즈와퍼").pack()
Button(frame_burger, text="몬스터X").pack()
Button(frame_burger, text="메가몬스터X").pack()

# 2. 음료
frame_drink = LabelFrame(root,text="음료")
frame_drink.pack(side="right", fill="both", expand=True)

Button(frame_drink, text="콜라").pack()
Button(frame_drink, text="제로콜라").pack()



root.mainloop()