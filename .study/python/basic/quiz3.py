# 매주 1회 작성해야 할 보고서가 있워요
# 다음과 같은 양식으로 매 주차보고서가 OO주차 보고서.txt로 저장되어야 합니다.

# - 00 주차 주간보고 -
# 부서:
# 이름:
# 업무 요약:

# 1 ~ 50 주차 보고서를 작성하는 후로그램을 맹글어 봅시다.

# for week in range(1, 51):
#     report_file = open("{0:0>2}주차.txt".format(week), "w", encoding="utf8")
#     print("\
#      - {0:0>2} 주차 주간보고 -".format(week), file=report_file)
#     print("부서: ", file=report_file)
#     print("이름: ", file=report_file)
#     print("업무 요약: ", file=report_file)
#     report_file.close()