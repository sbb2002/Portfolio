from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

listbox = Listbox(root, selectmode="extended", height=0)
# extended = 복수선택, single = 단수선택, height = 0이면 다 보일정도만
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()

def btncmd():
    # 삭제
    # listbox.delete(0 or END)
    
    # 갯수 확인
    # print("리스트에는", listbox.size(), "개가 있워요")

    # 항목 확인 (시작 idx, 끝 idx)
    # print("1번째부터 3번째까지의 항목: ", listbox.get(0, 2))    # index 0 ~ 2

    # 선택된 항목 확인 (위치로 반환, ex. (1,2,) )
    print("선택된 항목: ", listbox.curselection())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()