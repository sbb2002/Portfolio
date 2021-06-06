### windows only

import pyautogui

# fw = pyautogui.getActiveWindow()    # 현재 활성화된 창 정보 가져옴
# print(fw.title)     # 창 제목 정보
# print(fw.size)      # 창 크기 정보
# print(fw.left, fw.top, fw.right, fw.bottom)     # 창의 좌표 정보
# pyautogui.click(fw.left + 25, fw.top + 20)      # 현재 창의 원점으로부터 +

# for w in pyautogui.getAllWindows():
#     print(w)        # 모든 창 정보

# for w in pyautogui.getWindowsWithTitle("제목 없음"):
#     print(w)        # "제목 없음"인 이름을 모두 가져옴

w = pyautogui.getWindowsWithTitle("제목 없음")[0]
print(w)
if w.isActive == False:
    w.activate()    #창 활성화 (앞으로 띄우기)
    # 단 이미 앞에 있는 상태에서 최소화된걸 activate하면
    # 앞에 있다고 판단해서 동작안함

# 최대화, 최소화, 원상복구, 닫기
if w.isMaximized == False:
    w.maximize()

pyautogui.sleep(1)
# if w.isMinimized == False:
#     w.minimize()

w.restore()

w.close()