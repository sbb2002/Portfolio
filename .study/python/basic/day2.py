# # # def profile(name, age, main_lang):
# # #     print("이름: {0}\t나이: {1}\t주 사용 언어: {2}" \
# # #           .format(name, age, main_lang))
# # #
# # # profile("유재석", 20, "파이선")
# # # profile("김태호", 25, "자바")
# #
# # # 기본값 설정
# # def profile(name, age=17, main_lang="파이선"):
# #     print("이름: {0}\t나이: {1}\t주 사용 언어: {2}" \
# #           .format(name, age, main_lang))
# #
# # profile("유재석")
# # profile("김태호")
#
# # def profile(name, age, l1, l2, l3, l4, l5):
# #     print("이름: {0}\t나이: {1}\t".format(name, age), end=" ")
# #     print(l1, l2, l3, l4, l5)
#
# def profile(name, age, *language):
#     print("이름: {0}\t나이: {1}\t".format(name, age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()
#
# profile("유재석", 20, "Py", "Java", "C", "C++", "C#", "JavaScript")
# profile("김태호", 25, "Kotlin", "Swift")

gun = 10

def checkpoint(soliders):
    # gun = 20                  #local variable gun = not defined
    global gun                  #global variable gun = 10
    gun = gun - soliders
    print("[함수 내] 남은 총: {0}".format(gun))

def checkpoint_return(gun, soliders):
    gun = gun - soliders
    print("[함수 내] 남은 총: {0}".format(gun))
    return gun

print("전체 총: {0}".format(gun))
checkpoint(2)
print("남은 총: {0}".format(gun))
gun = checkpoint_return(gun, 2)