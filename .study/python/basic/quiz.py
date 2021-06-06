from random import *
customer = 1
take = 0
arriving_time = randint(5, 50)

while customer <= 100 :
    if arriving_time >= 5 and arriving_time <= 15 :
        print("[O] {0} 번째 손님 (소요시간: {1} 분)".format(customer, arriving_time))
        take += 1
    else:
        print("[ ] {0} 번째 손님 (소요시간: {1} 분)".format(customer, arriving_time))
    customer += 1
    arriving_time = randint(5, 50)
print("총 탑승 승객: {0} 명".format(take))
