from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "글자를 입력하시와요")

e = Entry(root, width=30)       # 한 줄 텍스트
e.pack()
e.insert(0, "한 줄만 입력해요옹")

def btncmd():
    # 내용 출력
    print(txt.get("1.0", END))      # LINE 1, COLUMN 0 (모든 글자를 가져와라)
    print(type(txt.get("1.0", END)))      # LINE 1, COLUMN 0 (모든 글자를 가져와라)

    print(e.get())

    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()