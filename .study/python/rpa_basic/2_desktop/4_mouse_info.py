import pyautogui
# pyautogui.mouseInfo()
# copy all
# 455,174 / 255,255,255 / #FFFFFF
# 좌표 / 색 좌표 /색 코드

# for i in range(10):
#     pyautogui.move(100, 100)
#     pyautogui.sleep(1)
    #마우스가 코드따라 동작 중인데
    #도중에 오류가 생겨서 강제 중단해야함
    #-> 모니터의 가장 끝 귀퉁이로 어떻게든 넣으면 강제 중단됨.
#pyautogui.FailSafeException: PyAutoGUI fail-safe triggered from mouse moving to a corner of the screen. To disable this fail-safe, set pyautogui.FAILSAFE to False. DISABLING FAIL-SAFE IS NOT RECOMMENDED.

#만일 이 중단법을 없애려면...
# pyautogui.FAILSAFE = False      # BUT! Not recommend!!
# for i in range(5):
#     pyautogui.moveTo(100,100)
#     pyautogui.sleep(1)

#모든 동작에 sleep(1) 적용. 알파고의 반속을 감동할 수 없을 때
# pyautogui.PAUSE = 1