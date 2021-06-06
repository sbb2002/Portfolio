class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self, to_name):
        print("안녕, " + to_name + "나는 ", self.name)

    def introduce(self):
        print("반갑습네다, " + self.name + " 그리고 나는 " + str(self.age) + " 살입네다.")

# 상속 안하고 쓰면...
# class Police:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def say_hello(self, to_name):
#         print("안녕, " + to_name + "나는 ", self.name)

#     def introduce(self):
#         print("반갑습네다, " + self.name + " 그리고 나는 " + str(self.age) + " 살입네다.")

#     def arrest(self, to_arrest):
#         print("You are under arrest! " + to_arrest)

# 상속을 사용하면...        
class Police(Person):
    def arrest(self, to_arrest):
        print("You are under arrest! " + to_arrest)
''' -> 공통성분은 상속을 쓰자. '''

class Programmer(Person):
    def program(self, to_program):
        print("이봐, 고든? 전에도 " + to_program + " 이걸 본 적 있지 않나?")

temmie = Person("뗌장인", 25)
waldo = Police("왈도! 힘세고 강한 아침!", 26)

temmie.say_hello("왈도쿤 ")
waldo.say_hello("뗌장인 ")

temmie.introduce()
waldo.introduce()

waldo.arrest("뗌장인")
temmie.program("왈도")