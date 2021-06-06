# 스크린샷 저장 프로그램
import time
from PIL import ImageGrab

time.sleep(5)   # 사용자가 준비하는 시간

for i in range(1, 11):  # 2초 간격으로 10개 이미지 저장
    img = ImageGrab.grab()  # 현재 스크린샷 가져옴
    img.save("image{}.png".format(i))   # 파일저장
    time.sleep(2)