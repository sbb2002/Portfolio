# # # # # # print("Python", "Java")
# # # # # # print("Python", "Java", sep=", ")
# # # # # # print("Python", "Java", sep=" vs ")
# # # # # # print("Python", "Java", sep=", ", end="? ")
# # # # # # print("무엇이 더 잼있을까여?")
# # # # # #
# # # # # # print("####################################")
# # # # #
# # # # # import sys
# # # # # print("Python", "java", file=sys.stdout)
# # # # # print("Python", "java", "를!", "에러가 났단다 얘!", sep=",", file=sys.stderr)
# # # # #
# # # #
# # # # scores = { "수학":0, "영어":50, "코딩":100 }
# # # # for subject, score in scores.items():
# # # #     # print(subject, score)
# # # #     print(subject.ljust(8), str(score).rjust(4), sep=": ")
# # # #
# # # # #대기 순번표
# # # # #001 002 003 004 ... 020
# # # # for num in range(1, 21):
# # # #     print("대기번호: "+str(num))
# # # #
# # # # #대기 순번표 비교
# # # # for num in range(1, 21):
# # # #     print("대기번호: "+str(num).zfill(3))
# # # #
# # # # answer = input("값을 입력하시오. ")
# # # # print("입력하신 값은 " + answer + " 입니다.")
# # #
# # # # 빈 자리는 여백으로 두고, 오른쪽 정렬을 하되 총 10 자리 공간을 확보
# print("{0: >10}".format(500))       # _: 빈칸, >: 오른쪽정렬, 10: 1칸, .foramt(500): 여백확보 후 500
# # print("{0: >+10}".format(500))      # +: format값이 양수이면 + 명시, 음수이면 - 명시
# # # print("{0: >+10}".format(-500))
# # # # 왼쪽정렬, 빈칸은 _로 표시
# print("{0:_<+10}".format(500))
# # # # 세 자리마다 , 찍어주기
# # # print("{0:+,}".format(1000000000000000000000000000000))      # ,만으로 자동 3자리 , 표시
# # # print("{0:+,}".format(-1000000000000000000000000000000))      # ,만으로 자동 3자리 , 표시
# # # # 세 자리마다 ,도 찍고 부호도 붙이고 30자릿수도 확보
# # # # 빈 칸은 ^로
# # # print("{0:^<+30,}".format(100000000))      # ,만으로 자동 3자리 , 표시
# # #
# # # # 소수점 출력
# # # print("{0:f}".format(5/3))
# # # print("{0:.2f}".format(5/3))
# # #
# # # # 파일 입출력
# # # score_file = open("score.txt", "w", encoding="utf8")        # score.txt를 write 목적으로 utf8로 인코딩하여 만듦
# # # print("수학 ; 0", file=score_file)                          # 수학점수를 score_file로 호출해 score.txt에 입력
# # # print("영어 ; 50", file=score_file)
# # # score_file.close()                                          # score.txt.를 닫음
# #
# # # score_file = open("score.txt", "a", encoding="utf8")        # score.txt를 append 목적으로 utf8로 인코딩하여 만듦
# # # score_file.write("과학 : 100")
# # # score_file.write("\n코딩 : 80")
# # # score_file.close()                                          # score.txt.를 닫음
# #
# # score_file = open("score.txt", "r", encoding="utf8")        # score.txt를 read 목적으로 utf8로 인코딩하여 만듦
# # # print(score_file.read())                                    # scoe.txt를 통쨰로 읽어옴
# # print(score_file.readline(), end="")                                    # scoe.txt를 1줄씩 읽어옴
# # print(score_file.readline(), end="")                                    # scoe.txt를 1줄씩 읽어옴)
# # print(score_file.readline(), end="")                                    # scoe.txt를 1줄씩 읽어옴)
# # print(score_file.readline())                                            # scoe.txt를 1줄씩 읽어옴)
# # score_file.close()                                          # score.txt.를 닫음
# #
# # # 만일 총 몇 줄인지 모를 경우는...
# # score_file = open("score.txt", "r", encoding="utf8")        # score.txt를 read 목적으로 utf8로 인코딩하여 만듦
# # while True:
# #     line = score_file.readline()
# #     if not line:
# #         break
# #     print(line, end="")
# # score_file.close()
# #
# # print(">..................<")
# #
# # # read한 줄을 list로 저장하기
# # score_file = open("score.txt", "r", encoding="utf8")        # score.txt를 read 목적으로 utf8로 인코딩하여 만듦
# # lines = score_file.readlines()                              # list로 저장
# # for line in lines:
# #     print(line, end="")
# # score_file.close()
# #
#
# #pickle
# import pickle
# # profile_file = open("profile.pickle", "wb")             #write binary(피클에 필요)
# # profile = {"이름":"박명수", "나이":"47", "취미":["축구", "골프", "코딩"]}
# # print(profile)
# # pickle.dump(profile, profile_file)                          #profile에 있는 정보를 file.에 저장
# # profile_file.close()
#
# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file)                           #profile.pickle에 있는 정보를 profile 에 저장
# print(profile)
# profile_file.close()


# with
import pickle
with open("profile.pickle", "rb") as profile_file:              # open한 것을 profile_file에 저장
    print(pickle.load(profile_file))                            # close 불필요

# with open("study.txt", "wb", encoding="utf8") as study_file:
#     study_file.write("파이손을 열심히 공부하고 잇워요")

with open("study.txt", "rb", encoding="utf8") as study_file:
    print(study_file.read())