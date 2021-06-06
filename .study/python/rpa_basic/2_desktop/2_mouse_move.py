import pyautogui

# 마우스 순간이동 (절대 좌표)
# pyautogui.moveTo(200, 100)      #지정위치로 마우스 이동 x, y coor.

# 마우스 이동    (절대 좌표)
# pyautogui.moveTo(100, 200, duration=5)  #등속도로 duration sec.동안 이동

# pyautogui.moveTo(100, 100, duration=0.25)
# pyautogui.moveTo(200, 200, duration=0.25)
# pyautogui.moveTo(300, 300, duration=0.25)
#
# # 상대 좌표로 이동
# pyautogui.moveTo(100, 100, duration=0.25)   #100, 100 로 순간이동
# print(pyautogui.position())
# pyautogui.move(100, 100, duration=0.25)     #현 위치(100,100)에서 +100,+100
# print(pyautogui.position())
# pyautogui.move(100, 100, duration=0.25)     #현 위치(200,200)에서 +100,+100
# print(pyautogui.position())

#좌표 확인
p = pyautogui.position()
print(p[0], p[1])
print(p.x, p.y)