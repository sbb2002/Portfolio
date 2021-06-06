import pyautogui

#스크린샷 찍기
# img = pyautogui.screenshot()
# img.save("screenshot.png")

# pyautogui.mouseInfo()
# 722,342 48,56,69 #303845

pixel = pyautogui.pixel(722,342)        #해당 픽셀의 정보를 가져옴
print(pixel)        #색 좌표

pxcolor = pyautogui.pixelMatchesColor(722,342, (48,56,69))    #좌표 = 색 좌표 비교
print(pyautogui.pixelMatchesColor(722,342, pixel))      #이렇게 해도 됨
print(pyautogui.pixelMatchesColor(722,342, (30,55,69)))

print(pxcolor)

#사이트 상에서 로그인할 때 픽셀 색 좌표를 이용해 매크로 작성 가능