import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

values=[str(i) + "일" for i in range(1, 32)]
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결제일")     # 최초 목록제목

# 텍스트 임의로 쓰기 불가
readonly_combobox = ttk.Combobox(root, height=5, values=values, state="readonly")
readonly_combobox.current(0)    # 0번째 idx 출력
readonly_combobox.pack()


def btncmd():
    print(combobox.get())
    print(readonly_combobox.get())

btn = Button(root, text="주문", command=btncmd)
btn.pack()

root.mainloop()