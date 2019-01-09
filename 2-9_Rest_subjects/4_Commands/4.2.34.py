lst=[]
lst_b=[]
n=int(input('количество студентов = '))
for i in range(n):
    fio=input('ФИО:')
    lst.append(fio)
lst_a=[i for i in lst if i[0] in["А","а","Е","Ё","ё","И","и","О","о",
"У","у","Ы","ы","Э","э","Ю","ю","Я","я"]]
lst_b=[i for i in lst if i not in lst_a]
print(lst_a, lst_b, sep='\n')
print("Более трех студентов с согласной буквы:", len(lst_b)>3)
