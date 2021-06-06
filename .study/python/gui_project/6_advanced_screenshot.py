# pip install keyboard

import time
import keyboard
from PIL import ImageGrab

def screenshot():
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time))   # image_년월일_시분초.png

keyboard.add_hotkey("F9", screenshot)   # F9누르면 스크린샷 저장

keyboard.wait("esc")    # 사용자가 esc누를 때까지 프로그램 수행