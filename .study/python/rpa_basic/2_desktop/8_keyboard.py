import pyautogui

w = pyautogui.getWindowsWithTitle("제목 없음")[0]   #메모장 1개 띄움
w.activate()

# pyautogui.write("12345")
# pyautogui.write("FUN!!", interval=0.25)     #한 글자 당 0.25초
#영문 및 숫자만 됨!!

# pyautogui.write(["t","e","s","t","left","left","right","l","enter"], interval=0.25)
# direction, enter = 키보드 커맨드

# https://automatetheboringstuff.com/2e/chapter20/
# Table 20-1: PyKeyboard Attributes 참고

# 특수 문자
# shift + 4 = $
pyautogui.keyDown("shift")
pyautogui.press("4")
pyautogui.keyUp("shift")

# 조합키 (hot key)
# ctrl + A
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a")
# pyautogui.keyUp("ctrl")

# 그러나 이러면 너무 길고 복잡해지므로 다음처럼 쓴다
# pyautogui.hotkey("ctrl","alt","shift","a")
# Push on (ctrl > alt > shift > a) > Push off (ctrl > alt > shift > a)
# pyautogui.hotkey("ctrl","a")

# 한글 입력 (need: pip install pyperclip )
import pyperclip
# pyperclip.copy("나도코딩")      # 글자를 클립보드에 저장
# pyautogui.hotkey("ctrl","v")

# 줄여서 쓰려면 def 이용
def hangul(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl","v")

hangul("나도코딩")

# 키보드로 매크로 프로세스 긴급종료
# win : ctrl + alt + del
# max : cmd + shift + option + q