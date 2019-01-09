import random
list1=[]
list2=[]
list1.append(19.85)
list1+=[0.14,45.,8.64]
list2.extend(list1[1:4])
list2.insert(3,22.44)
list1.insert(2, 1)
list1.insert(4, 0)
list2.insert(2, 0)
list2.insert(4, 44)
print('Исходные списки:\n1й: {}\n2й: {}'.format(list1,list2))
del list1[0]
del list2[0]
list1.remove(random.choice(list1))
list2.remove(random.choice(list2))
print('После удалений:\n1й: {}\n2й: {}'.format(list1,list2))
set1=set(list1)
set2=set(list2)
unique_set1=set1.intersection(set1.difference(set2))
unique_set2=set2.intersection(set2.difference(set1))
obsh_set=set1.intersection(set2)
print('Общие элементы:', obsh_set)
print('Уникальные элементы:\n1й: {}\n2й: {} \n'.format(unique_set1,unique_set2))
list3=list1+list2
print('3й: ', list3)
list3.sort()
print('Сортированный:',list3)
list3.reverse()
print('Обратный: ',list3)
print('Среднее арифметическое: {:.2f}'.format(sum(list3[2::2])/len(list3[2::2])))
print('Среднее алгебраическое:', list3[1]*list3[3]*list3[5]*list3[7]/len(list3[1::2]))
print('Максимальный :',list3[0])
print('Минимальный :',min(list3))

