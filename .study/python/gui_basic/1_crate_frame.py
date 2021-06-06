from tkinter import *

root = Tk()
root.title("Nado GUI")
# root.geometry("640x480")            #가로 * 세로
root.geometry("640x480+100+100")    #가로 * 세로 + x좌표 + y좌표

root.resizable(False, False)        #너비, 높이 변경 불가 (창 크기조절 x)

root.mainloop()