# TODO: 
# FIXME:
'''
< 이름표기법 >

PascalCase: 클래스 이름
snake_case: 변수, 함수 이름
camelCase: 파이썬에서 잘 안씀

'''

class Cake:
    ''' 케익을 나타내는 클래스 -> 속성 '''
    coat = '생크림'

# print(Cake)     # <class '__main__.Cake'>: __main__(이 파일의).Cake 클래스


### 인스턴스 만들기
cake_1 = Cake()     #class Cake의 인스턴스1
cake_2 = Cake()     #class Cake의 인스턴스2

# print(type(cake_1))
# print(isinstance(cake_2, Cake)) #cake_2는 Cake의 인스턴스인가? T/F

# id는 해당 클래스나 인스턴스의 메모리 주소값을 알려준다. (항상 바뀜)
print(id(Cake))         # 1826 9347 34496 번지
print(id(cake_1))       # 1826 9413 07776 번지
print(id(cake_2))       # 1826 9413 54624 번지


### 클래스와 인스턴스의 속성(attr) 읽기
print("class Cake의 attr: \t" + Cake.coat)
print("inst. cake_1의 attr: \t" + cake_1.coat)
print("inst. cake_2의 attr: \t" + cake_2.coat)
print("##############################################")
''' 생크림으로 나온다.
    그런데 class Cake의 coat속성을 초콜릿으로 수정하면 어떻게 될까?    '''

Cake.coat = "초콜릿"    # attr 수정
Cake.price = 4000      # attr 추가

print("class Cake의 attr. coat: \t" + Cake.coat)
print("inst. cake_1의 attr. coat: \t" + cake_1.coat)
print("inst. cake_2의 attr. coat: \t" + cake_2.coat)

print("class Cake의 attr. price: \t" + str(Cake.price))
print("inst. cake_1의 attr. price: \t" + str(cake_1.price))
print("inst. cake_2의 attr. price: \t" + str(cake_2.price))
''' 모체가 되는 class Cake를 수정했더니 자식이 되는 inst.들이 같이 수정, 추가되었다. '''

print("##############################################")


### 인스턴스 전용 속성
cake_1.topping = '블루베리'     #inst. cake_1의 attr. topping을 추가
print("inst. cake_1의 전용attr: \t" + cake_1.topping)   # 블루베리

# print("inst. cake_2의 전용attr: \t" + cake_2.topping)       # AttributeError: 'Cake' object has no attribute 'topping'
# print("class Cake의 전용attr: \t" + Cake.topping)           # AttributeError: type object 'Cake' has no attribute 'topping'

cake_1.coat = "아이스크림"
print(cake_1.coat)
print(Cake.coat)
print(cake_2.coat)
''' inst. cake_1 만 초콜릿 > 아이스크림 으로 수정되었다. '''

print("##############################################")

### dir() 함수로 이름공간에 정의된 이름 구하기
import pprint
pprint.pp(dir(Cake))
''' 아까 정의한 coat, price말고도 __***___로 정의된 것들이 많이 있다. '''
''' 이것들은 class로서 자동으로 정의된 것들이다.                      '''

print("##############################################")


### 메서드 (def)
class Cake:
    coat = "생크림"

    def describe(self):
        ''' 이 케익에 대한 정보를 묘사 '''
        # print("이 케익은", Cake.coat, "으로 덮여있다.")
        print("이 케익은", self.coat, "으로 덮여있다.")

# print(Cake.describe())      # 이 케익은 생크림 으로 덮여있다.

cake_1 = Cake()
cake_1.coat = "초콜릿"

# print(cake_1.describe())    # TypeError: describe() takes 0 positional arguments but 1 was given
''' 
    describe()는 인자(idx) 0개가 필요한데, 1개가 주어졌다. 
    idx를 준 적도 없는데 1개를 줬었다???
    사실, 클래스 기준으로 호출할 때와 인스턴스 기준으로 호출할 때 그 방식이 다르기 때문이다.
    
    inst.에서 def를 호출하면...
    암묵적으로 메서드 호출의 기준이 되는 inst. 그 자체(cake_1)가 첫번째 idx(self)로 메서드에 전달된다.
    self라는 idx가 전달되었는데 def 내에서 사용하지 않는다.
    그래서 0개가 필요한데 1개가 주어졌다고 표시하는 것이다.

    게다가 def describe(): ... Cake.coat ... 로 되어있다.
    inst. cake_1의 입장에서는 외부에 있는 class Cake를 인식하지 못한다.
    어찌보면 에러나는게 당연지사.

    아무튼 이를 방지하려면 자기 자신(self)를 호출해서 해결한다. <ln 84번 참조>
    애초에 인스턴스를 사용하려는 목적으로 클래스를 사용하기에 이렇게 사용하는 것이 보편적이다.
    
    self를 사용한 이후부터, ln 86는 이제 에러가 나게 된다. 유의할 것.
        ㄴTypeError: describe() missing 1 required positional argument: 'self'
    이를 해결하고 싶다면 새로 def를 작성해 self가 없을 때처럼 지으면 된다.

    정리 >>>
        self O ---> inst.method()
        self X ---> class.method()
'''
cake_1.describe()        #이 케익은 초콜릿 으로 덮여있다. well done!
# self를 이용하는 것은 class 조작보다는 inst. 조작을 위한 것일 때가 많다.
# 그러므로 ln 79처럼 inst. 기준의 메서드를 호출하려고 self를 썼는데, 
# class 기준의 호출하려니 에러가 날 수 밖에.

print("##############################################")


### 인스턴스 초기화

# cake_1 = Cake()
# cake_2 = Cake()
# cake_3 = Cake()
# ...
# cake_1.candles = 0
# cake_2.candles = 0
# cake_3.candles = 0
# ...               -> 케익이 너무 많아지면 너무나 불편하다.
''' 
그래서 __init__()를 이용해 초기화하는 트릭을 쓴다. 

cake_n = Cake() ---> 인스턴스화를 명령하면 아래와 같은 단계를 수행한다.
1. __new__() = 메서드를 실행해 새 객체를 만듦. 기본으로 제공되기에 따로 정의x
2. __init__() = 메서드를 실행해 객체를 초기화.

'''

class Cake:
    """케익을 나타내는 클래스"""
    coat = '생크림'
    
    # candles을 초기화하고 인스턴스가 주는 값에 따라 새로 정의
    def __init__(self, candles):                          
        """인스턴스를 초기화한다."""
        self.candles = candles
    
    def describe(self):
        """이 케익에 관한 정보를 화면에 출력한다."""
        print('이 케익은', self.coat, '으로 덮여 있다.')
        print('초가', self.candles, '개 꽂혀 있다.')

cake_1 = Cake(12)
cake_2 = Cake(100)

print('케익 1:')
print('초 개수:', cake_1.candles)
print("")
print('케익 2:')
cake_2.describe()

print("##############################################")

# 좀더 활용하면 이렇게 쓸 수 있다.

class Cake:
    """케익을 나타내는 클래스"""
    coat = '생크림'
    
    # inst. = Cake(topping, price, candles(선택))
    def __init__(self, topping, price, candles=0):
        """인스턴스를 초기화한다."""
        self.topping = topping   # 케익에 올린 토핑
        self.price = price      # 케익의 가격
        self.candles = candles  # 케익에 꽂은 초 개수
    
    def describe(self):
        """이 케익에 관한 정보를 화면에 출력한다."""
        print('이 케익은', self.coat, '으로 덮여 있다.')
        print(self.topping, '을 올려 장식했다.')
        print('가격은', self.price, '원이다.')
        print('초가', self.candles, '개 꽂혀 있다.')

cake_1 = Cake('눈사람 사탕', 10000)
cake_2 = Cake('한라봉', 9000, 8)

print('케익 1:')
cake_1.describe()
print("")
print('케익 2:')
cake_2.describe()