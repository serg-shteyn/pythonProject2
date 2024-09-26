import random
# Дополнительное практическое задание по модулю: "Основные операторы"

insert_list = []
for i in range(3,21):
	insert_list.append(i) #Создаем список чисел для первой вставки
	
n = random.choice(insert_list)
print(f'В первой вставке выпало: {n}')
result=[] #создаем пустой список для пароля
for j in range(1,n+1):
	for k in range(j+1,n+1):
		if n % (j+k) == 0:
			result.append(j)
			result.append(k)
print('Пароль: ')
print(*result)