# # 계산기
# try:
#     print("나누어보와요")
#     nums = []
#     nums.append(int(input("1번째: ")))
#     nums.append(int(input("2번째: ")))
#     # nums.append(int(nums[0]/nums[1]))
#     print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
# except ValueError:
#     print("으읶! 숫자를 쓰세오!")
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:
#     print("이게 모오지???")
#     print(err)

class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg

# 의도적 에러
try:
    print("한 자리용 나누기 계산기입네다.")
    num1 = int(input("1st number: "))
    num2 = int(input("2nd number: "))
    if num1 >=10 or num2 >= 10:
        # raise ValueError        #if 만족시 강제로 ValueError로 넘어감
        raise BigNumberError("입력값: {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, num1/num2))
except ValueError:
    print("두 자릿수 이상을 입력햇워요. 한 자릿수만 쓰세^오^")
except BigNumberError as err:
    print("한 자릿수만 쓰세^오^")
    print(err)
finally:
    print("계산기를 사용해주셔서 감쟈함미다...")