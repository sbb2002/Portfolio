# 일반 유닛 클래스
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))



# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 30)
# wraith1 = Unit("레이스", 80, 5)
#
# print("유닛 이름: {0} , 공격력: {1}".format(wraith1.name, wraith1.damage))
#
# # 마인드컨트롤을 함. 이 유닛은 클로킹 보유
# wraith2 = Unit("탈취한 레이스", 80, 5)
# wraith2.clocking = True
#
# if wraith2.clocking == True:
#     print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))
#

# 공격 유닛 클래스 ( Unit 상속 )
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} 유닛이 파괴되었습니다.".format(self.name))

# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")           # 어택 땅
# firebat1.damaged(25)             # 데미지받음
# firebat1.damaged(25)             # 데미지받음

# 공중유닛 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
              .format(name, location, self.flying_speed))

# 공중유닛 (공격가능) 클래스 ( 다중 상속 )
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)      #지상 속도 = 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)
# 발키리
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")

# 벌쳐
vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루져
battlecruiser = FlyableAttackUnit("배틀크루져", 500, 25, 3)

vulture.move("11시")
battlecruiser.fly(battlecruiser.name, "9시")

# 연산자 오버로딩을 통해 move와 fly가 동시로 되게끔 가능
battlecruiser.move("9시")

# pass
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)      #상속 시 명시적으로 받을 수 있다.
        super().__init__(name, hp, 0)           #윗줄과 동일한 기능 ( 단, 다중상속 시 첫 상속만 받고 뒤는 무시
        self.lcoation = location
        # pass
#
# # 서플라이 디폿
# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")
#
# def game_start():
#     print("[알림] 게임이 시작되었습니다.")
#
# def game_over():
#     pass
#
# game_start()
# game_over()

# super
