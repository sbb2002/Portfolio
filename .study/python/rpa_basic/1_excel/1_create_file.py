from openpyxl import Workbook
wb = Workbook() #새 워크북 생성 = 방금 킨 새 엑셀 파일 같음
ws = wb.active  #현재 활성화된 sheet가져옴
ws.title = "NadoSheet"      #sheet이름변경
wb.save('sample.xlsx')
wb.close()