sentence=input('counting vowels: \n')
vowels=["А","Е","Ё","И","О","У","Ы","Э","Ю","Я","а","е","ё","и","о","у","ы","э","ю","я"]
count = 0
for i in sentence:
    if i not in vowels:
        continue
    count+=1

print('amount of vowels =', count)
