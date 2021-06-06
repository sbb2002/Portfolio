# 일반 가격
def price(people):
    print("[일반] {0} 명 가격: {1} 원입니다.".format(people, people * 10000))

# 조조 할인 가격
def price_morning(people):
    print("[조조] {0} 명 가격: {1} 원입니다.".format(people, people * 6000))

# 군인 할인 가격
def price_soldier(people):
    print("[군인] {0} 명 가격: {1} 원입니다.".format(people, people * 5000))