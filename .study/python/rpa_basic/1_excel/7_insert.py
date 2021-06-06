from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

#엑셀 상 8번줄에 row 추가
# ws.insert_rows(8)
# ws.insert_rows(8, 5)     #8번째 줄에 5줄 추가
# wb.save("sample_insert_rows.xlsx")

#이번에는 cols
ws.insert_cols(2, 3)
wb.save("sample_insert_cols.xlsx")
