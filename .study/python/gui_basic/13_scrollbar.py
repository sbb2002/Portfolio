from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# set이 없으면 스크롤을 내려도 다시 올려옴. yscroll첨가와 맵핑이 필요
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)     # 맵핑(움직임, 위치 동기화)

for i in range(1,32):
    listbox.insert(END, str(i) + "일")
listbox.pack(side="left")


root.mainloop()