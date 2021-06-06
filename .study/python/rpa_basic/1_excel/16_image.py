from openpyxl import Workbook
from openpyxl.drawing.image import Image
wb = Workbook()
ws = wb.active

img = Image("img.png")     # 16_image.py 이 파일과 동일한 경로에 img.png가 있어야됨.

ws.add_image(img, "C3")

wb.save("sample_image.xlsx")
