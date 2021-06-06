import pyautogui

# 시작 + shift + s : 캡쳐도구

# file_menu = pyautogui.locateOnScreen("file_menu.png")
# print(file_menu)
# pyautogui.click(file_menu)  #이미지의 중간부분 클릭

# close_icon = pyautogui.locateOnScreen("close_terminal.png")
# pyautogui.moveTo(close_icon)

# screen = pyautogui.locateOnScreen("screenshot.png") #못찾으면 None
# print(screen)

#만약 동일 icon이 여러개 있다면???
# for i in pyautogui.locateAllOnScreen("checkbox.png"):
#     print(i)
#     pyautogui.click(i, duration=0.25)      #checkbox icon을 모두 찾아 클릭해줌 ㅎ

#밑은 단 한번만 시도하고 끝
# checkbox = pyautogui.locateOnScreen("checkbox.png")
# pyautogui.click(checkbox)




#이 방법은 해상도나 픽셀의 미묘한 차이가 나면 인식하지 못함;;

#이미지 처리 - 속도 개선
#전체화면이 넓어서 조금 느림...
#그래서 속도개선을 위해 여러 방법이 있다!

#1. GrayScale (30% 향상, 정확도 저하)
# close_icon = pyautogui.locateOnScreen("close_terminal.png", grayscale=True)
# pyautogui.moveTo(close_icon)

#2. 범위 지정
# close_icon = pyautogui.locateOnScreen("close_terminal.png", region=(60,690,847,24))
# pyautogui.moveTo(close_icon)

# 60,690
# 907,714

#> 정확도 조정 (정확도 기준 낮게 잡아주기)
# bug_btn = pyautogui.locateOnScreen("bug.png", confidence=0.9)   #신뢰도 조절
# pyautogui.moveTo(bug_btn)      #못찾음




#자동화 대상이 바로 보여지지 않는 경우
# 1. 계속 하염없이 기다리기
# file_menu_notepad = pya
# utogui.locateOnScreen("file_menu_notepad.png")
# if file_menu_notepad:
#     pyautogui.click(file_menu_notepad)
# else:
#     print("발견 실패")      #너무 빨라서 거의 항상 여기로 타게됨

#while로 오랫동안 돌려둘 수 있다.
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     print("발견 실패")
#
# pyautogui.click(file_menu_notepad)

# 2. 타임아웃
import time
import sys

# timeout = 10    #10초 대기
# start = time.time()
# file_menu_notepad = None
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     end = time.time()
#     if end - start > timeout:   #10초 초과 시
#         print("시간초과")
#         sys.exit()              #종료시킴

def find_target(img_file, timeout=30):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break
    return target

def my_click(img_file, timeout=30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f"[Timeout {timeout}s] Target not found ({img_file}). Terminate program.")
# pyautogui.click(file_menu_notepad)

my_click("file_menu_notepad.png", 1)