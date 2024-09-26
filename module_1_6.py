# словари

my_dict = {'Максим': 2018, 'Артём': 2019, 'Сергей': 1980}
print('Словарь :',my_dict)
print('год рождения Артёма -',my_dict['Артём'])
print('год рождения Светланы -',my_dict.get('Светлана'))
my_dict['Светлана']=1984
my_dict['Михаил']=1955
a = my_dict.pop('Артём')
print('Год рождения удаленного :',a)
print('Измененный словарь :',my_dict)
print()
#множества

my_set = {2,5,73,2,3,5,9,'cat'}
print('Множество :',my_set)
my_set.add(88)
my_set.add(99)
my_set.discard(2)
print('Измененное множество :',my_set)