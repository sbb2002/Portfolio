import pyautogui

# print("곧 시작됩니다...")
# pyautogui.countdown(3)
# print("자동화 시작")

# pyautogui.alert("자동화 수행을 실패하였습니다.", "경고!")      # 확인버튼만 있는 팝업
# result = pyautogui.confirm("계속 진행하시겠습니까?", "확인")
# print(result)   #확인 = OK, 취소 = Cancel

# result = pyautogui.prompt("파일명을 무엇으로 하시겠습니까?", "입력")
# print(result)   #Cancel = None, Ok = 적은대로

result = pyautogui.password("암호를 입력하세요")
print(result)       #위와 같으나 *******로 비밀화됨

# https://pyautogui.readthedocs.io/en/latest/
# 이 사이트에서 pyautogui에 대해 자세히 배울 수 있다.