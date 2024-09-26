students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]

students=sorted(students) #сортируем студентов в алфавитном порядке в список
grades = list(map(lambda x: sum(x)/len(x), grades)) #считаем среднее значение оценок и записываем в томже порядке в список
dict_students=dict(zip(students,grades))
print(dict_students) #объдиняем списки студентов и их средних оценок