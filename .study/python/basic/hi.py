# # # # # print("대기번호 : 1")
# # # # #
# # # # # for waiting in range(10):
# # # # #     for a in range(5):
# # # # #         print("대기번호 : {0}{1}".format(waiting,a))
# # # #
# # dict = ("Blue Mary", "최번개", "장거한")
# #
# # for winner in dict:
# #     print("Winner is {0}!!".format(winner))
# #
# # # menu = {"우유", "커피", "쥬스"}
# # # print(menu, type(menu))
# # #
# # # menu = list(menu)
# # # print(menu, type(menu))
# # #
# # # menu = tuple(menu)
# # # print(menu, type(menu))
# # #
# # # menu = set(menu)
# # # print(menu, type(menu))
# # #
# # # weather = input("오늘 날씨는 어때요?")
# # # if weather == "rainy" or weather == "snowy":
# # #     print("우산을 챙기세요")
# # #     if not weather ==  "rainy":
# # #         print("장갑도 챙기세요")
# # # elif weather == "smog":
# # #     print("마스크를 쓰세요")
# # # elif weather == "thunder":
# # #     print("벼락 조심하세요")
# # # else:
# # #     print("날씨가 좋네요")
# #
# customer = "응가맨"
# index = 5
# while index >= 1:
#     print("{0} 고갸끄사마, 고히ㅡ 찾아가는데스웅. {1}번만에 찾아가는데스웅".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("갖다버린데스웅")
#
# customer = "구구"
# print("{0} 님, 주문하신 커피가 나왔습니다.".format(customer))
# answer = "UNKNOWN"
# while answer != "네":
#     answer = input("커피 주문하신 {0} 님, 맞으신가요?".format(customer))
#     if answer != "네" :
#         print("아직 음식이 나오지 않았습니다.")
# print("커피 여기 있습니다. 맛있게 드십시오.")

def open_account():
    print("새 계좌가 생성되었읍니다.")

def deposit(balance, money):
    print("{0} 원 입금되었습니다. 잔액은 {1} 원입니다.".format(money, balance + money))
    return balance + money

def withdraw(balance, moeny):
    if balance >= money :
        print("{0) 원 출금되었습니다. 잔액은 {1} 원입니다.".format(money, balance - money))
        return balance - money
    else:
        print("잔액이 모자라 출금할 수 없습니다. 현재 잔고 {0} 원".format(balance))
        return balance

def withdraw_night(balance, money):
    commission = 1000
    return commission, balance - money - commission

balance = 0
balance = deposit(balance, 100000)
commision, balance = withdraw_night(balance, 10000)
print("수수료는 {0} 원 이며, 잔액은 {1} 원 입니다.".format(commision, balance))