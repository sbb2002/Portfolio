from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

#7번 학생이 전학갔음
# ws.delete_rows(8)
# ws.delete_rows(8, 3)    #8번째 줄부터 3줄 삭제
# wb.save("sample_delete_row.xlsx")

# ws.delete_cols(2)       #영어 점수 열 ( B ) 삭제
ws.delete_cols(2, 2)       #점수 다 삭제

wb.save("sample_delete_col.xlsx")