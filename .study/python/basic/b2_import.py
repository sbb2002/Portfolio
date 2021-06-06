import b2_module

print(b2_module.hello('superman'))

print(__name__)     # 자기 자신을 실행하면 __main__, 그 외에는 *.py

''' 
    import로 불러온 모듈 속 __name__ == b2_module.py 
    따라서 __name__ != __main__ 이기 때문에 모듈 속 hello('batman')은 실행되지 않는다.

'''