kor = ["사과", "오렌지", "바나나"]
eng = ["apple", "orange", "banana"]

print(list(zip(kor, eng)))

mixed = [('사과', 'apple'), ('오렌지', 'orange'), ('바나나', 'banana')]
print(list(zip(*mixed)))  # *들어가면 unzip

kor2, eng2 = zip(*mixed)
print(kor2)
print(eng2)