# 맛있는 치킨집
# 자동주문 시스템 개발
# 시스템 코드를 확인하고 적절한 예외처리 구문을 넣을 것.

# 조건1: 1보다 작거나 숫자가 아닌 값이 들어오면 ValueError로 처리
#         출력 메시지: "잘못된 값을 입력했읍니다.
# 조건2: 대기손님이 주문할 수 있는 총 치킨은 10마리로 한정
#         치킨 전량 소진 시, 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
#         출력 메시지: "재고가 소진되어 더 이상 주문을 받을 수 없읍니다..."

class SoldOutError(Exception):
    # def __init__(self, msg):
    #     self.msg = msg
    # def __str__(self):
    #     return self.msg
    pass
chicken = 10
waiting = 1

# 이 구문은 while을 오질라게 돌리다가 err가 나면 except로 가버림.
# try:
#     while(True):
#         print("\n[남은 치킨: {0} 마리]".format(chicken))
#         if chicken < 1:
#             raise SoldOutError("재고가 소진되어 더 이상 주문을 받을 수 없읍니다...")
#         order = int(input("치킨을 몇 마리 주문하시겠읍니까? "))
#         if order < 1:
#             raise ValueError
#         elif order > chicken:
#             print("재료가 부족합니다.")
#         else:
#             print("[대기번호: {0}] {1} 마리 주문이 완료되었읍니다. 잠시만 기다려주세요."\
#                   .format(waiting, order))
#             waiting += 1
#             chicken -= order
# except ValueError:
#     print("잘못된 값을 입력했읍니다...")
# except SoldOutError as err:
#     print(err)
# finally:
#     print("우리 치킨집을 찾아주셔서 감사합니다.\n")



# 이 구문은 while을 오질라게 돌리다 err이 나도 except가 내부에 있기에 다시 while이 돌아감. break 필.
while(True):
    try:
        print("\n[남은 치킨: {0} 마리]".format(chicken))
        if chicken < 1:
            raise SoldOutError
        order = int(input("치킨을 몇 마리 주문하시겠읍니까? "))
        if order < 1:
            raise ValueError
        elif order > chicken:
            print("재료가 부족합니다.")
        else:
            print("[대기번호: {0}] {1} 마리 주문이 완료되었읍니다. 잠시만 기다려주세요."\
                  .format(waiting, order))
            waiting += 1
            chicken -= order
    except ValueError:
        print("잘못된 값을 입력했읍니다...")
    except SoldOutError:
        print(("재고가 소진되어 더 이상 주문을 받을 수 없읍니다..."))
        break
    finally:
        print("우리 치킨집을 찾아주셔서 감사합니다.\n")