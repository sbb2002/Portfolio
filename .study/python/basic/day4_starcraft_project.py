from random import *

# 일반 유닛 클래스
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0}이 생성되었습니다.".format(name))

    def move(self, location):
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        if self.hp > 0:
            print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        else:
            print("{0} 유닛이 파괴되었습니다.".format(self.name))

# 공격 유닛 클래스
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))

# 공중유닛 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
              .format(name, location, self.flying_speed))

# 공중유닛 (공격가능) 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)      #지상 속도 = 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        self.fly(self.name, location)

# 빌딩유닛
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)      #상속 시 명시적으로 받을 수 있다.
        super().__init__(name, hp, 0)           #윗줄과 동일한 기능 ( 단, 다중상속 시 첫 상속만 받고 뒤는 무시
        self.lcoation = location


# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0}이 스팀팩을 사용합니다. [HP {1}]".format(self.name, self.hp))
        else:
            print("{0}이 스팀팩을 사용할 수 없습니다. (HP 부족)".format(self.name))

# 시즈탱크
class Tank(AttackUnit):
    seize_developed = False     #시즈모드 개발여부
    seize_mode = False
    def __init__(self):
        AttackUnit.__init__(self,"시즈탱크", 150, 1, 35)
    def set_seize_mode(self):                   #시즈모드 명령
        if Tank.seize_developed == False:       #개발 안되었을 시 되돌아감
            return
        #시즈모드가 아닐 때 -> 시즈모드로 전환
        if self.seize_mode == False:
            print("{0}가 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        #시즈모드일 때 -> 시즈모드 해제
        else:
            print("{0}가 시즈모드로 전환합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False

# 레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False        #클로킹 해제상태
    def clocking(self):
        if self.clocked == True:
            print("{0}가 클로킹을 해제합니다.".format(self.name))
            self.clocked = False
        else:
            print("{0}가 클로킹을 합니다.".format(self.name))
            self.clocked = True

def game_start():
    print("[알림] 게임이 시작되었습니다.")

def game_over():
    print("Player : gg")
    print("[Player]님이 게임에서 나갔습니다.")

### 실제게임 ###
game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

# 유닛 일괄 정리
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 부대 이동
for unit in attack_units:
    unit.move("1시")

# 시즈모드 개발
Tank.seize_developed = True
print("[알림] 시즈탱크의 [시즈모드]가 개발되었습니다.")

# 공격모드 준비 (마린: 스팀팩사용, 탱크: 시즈모드, 레이스: 클로킹)
for unit in attack_units:
    if isinstance(unit,Marine):     #현재 유닛이 마린이면
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

# 부대 일제공격
for unit in attack_units:
    unit.attack(("1시"))

# random한 피해를 입음
for unit in attack_units:
    unit.damaged(randint(5, 91))    # 5 ~ 20 사이에서 데미지 받음

# 다 주것따.. 게임 끗. 서렌
game_over()