# tkinter를 이용한 메모장 프로그램을 만들어봅시다.

# [GUI 조정]
# 1. title: 제목 없음 - Windows 메모장
# 2. 메뉴: 파일, 편집, 서식, 보기, 도움말
# 3. 실제 메뉴 구현: 파일 메뉴 내에서 열기, 저장, 끝내기 3개만 처리
#     3-1. 열기: mynote.txt 파일내용을 열어서 보여주기
#     3-2. 저장: mynote.txt 파일에 현재 내용 저장하기
#     3-3. 끝내기: 프로그램 종료
# 4. 프로그램 시작 시 본문은 빈 상태
# 5. 하단 status 바는 필요없음
# 6. 프로그램 크기, 위치는 자유롭게 하되 크기조정 가능해야 함
# 7. 본문 우측에 상하 스크롤 바 넣기

import sys, os
import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("제목 없음 - Windows 메모장")
root.geometry("640x480")

# 스크롤바 및 메모장
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")
txt = Text(root, width=100, height=100, yscrollcommand=scrollbar.set)
txt.pack(side="left", expand=True)
scrollbar.config(command=txt.yview)

# 메뉴
menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_edit = Menu(menu, tearoff=0)
menu_style = Menu(menu, tearoff=0)
menu_view = Menu(menu, tearoff=0)
menu_help = Menu(menu, tearoff=0)


# 파일 메뉴 내 기능 구현
def openfile():
    with open("mynote.txt", "r", encoding="utf-8") as f:
        txt.delete("1.0", END)    
        txt.insert(END, f.read())
        
def savefile():
    with open("mynote.txt", "w", encoding="utf-8") as f:
        f.write(txt.get("1.0", END).strip())

def exit_program():
    f = open("mynote.txt", "r", encoding="utf-8")
    data = f.read()
    f.close()
    if txt.get("1.0", END).strip() == data:
        sys.exit()
    else:
        response = msgbox.askyesno("저장", "저장하시겠습니까?\n저장하지 않은 작업은 모두 손실됩니다.")
        if response == True:
            savefile()
            sys.exit()
        elif response == False:
            sys.exit()

# =============================================================
# filename = "mynote.txt"
# def openfile2():
#     if os.path.isfile(filename):    # 있으면 T, 없으면 F
#         with open(filename, "r", encoding="utf8", ) as file:
#             txt.delete("1.0", END)
#             txt.insert(END, file.read())

# def savefile2():
#     with open(filename, "w", encoding="utf8") as file:
#         file.write(txt.get("1.0", END))
# =============================================================

menu_file.add_command(label="열기", command=openfile)
menu_file.add_command(label="저장", command=savefile)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=exit_program)     #command=root.quit(정의불필요)을 해도 된다. 단, 섬세하게 동작하려면 이대로.

# 기능 도입
menu.add_cascade(label="파일", menu=menu_file)
menu.add_cascade(label="편집", menu=menu_edit)
menu.add_cascade(label="서식", menu=menu_style)
menu.add_cascade(label="보기", menu=menu_view)
menu.add_cascade(label="도움말", menu=menu_help)

root.config(menu=menu)


root.mainloop()