def std_weight(height, gender):
    if gender == "man":
        weight = round(((height/100) ** 2) * 22, 2)
        print("키 {0} cm 남성의 표준체중은 {1} kg입니다.".format(height, weight))
    elif gender == "woman":
        weight = round(((height/100) ** 2) * 21, 2)
        print("키 {0} cm 여성의 표준체중은 {1} kg입니다.".format(height, weight))
    else:
        print("성별은 ( man / woman )만 고르실 수 있습니다. 다시 시도해주세요.")

gender = input("man입니까, woman입니까?")
height = int(input("당신의 키는 몇 cm입니까?"))
std_weight(height, gender)