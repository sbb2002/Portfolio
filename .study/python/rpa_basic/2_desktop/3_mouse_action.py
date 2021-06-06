import pyautogui
pyautogui.sleep(3)      #3초 대기
# print(pyautogui.position())

# pyautogui.click(64, 17, duration=1)     #pycharm의 file 버튼 위치

# 드래그 앤 드랍 활용가능
# pyautogui.mouseDown()   #클릭 홀드
# pyautogui.mouseUp()     #클릭 홀드 해제

# pyautogui.doubleClick()
# pyautogui.click(clicks=500)   #위와 같은 더블클릭 가능, 그 이상 매크로질 가능

# pyautogui.moveTo(200, 200)
# pyautogui.mouseDown()
# pyautogui.moveTo(300, 300)
# pyautogui.mouseUp()

# pyautogui.rightClick()      #오른쪽 클릭
# pyautogui.middleClick()     #휠 클릭
# pyautogui.moveTo(x=1373, y=628)
# pyautogui.drag(100, 0, duration=0.25)       #상대위치로 연산, duration이 있으면 드래그가 됨. 없을 시 드래그가 안될 수 있음
# pyautogui.dragTo(1000, 514, duration=0.25)                 #절대좌표로 이동, 마찬가지로 duration필요

# pyautogui.scroll(300)   #스크롤 위로 300
# pyautogui.scroll(-500)   #스크롤 아래로 300
