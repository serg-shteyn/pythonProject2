#Создание функций на лету
#Цель: освоить на практике замыкание, объекты-функторы и lambda-функции.
from random import choice


first = 'Мама мыла раму'
second = 'Рамена мало было'

#Lambda-функция:
result=map(lambda x,y:x==y,first,second)
print(list(result))

#Замыкание:
def get_advanced_writer(file_name):
	def write_everything(*data_set):
		for i in data_set:
			with open(file_name,'a') as file:
				file.write(f"{i}\n")
	return write_everything
	
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

#Метод __call__:
class MysticBall:
	
	def __init__(self,*words):
		self.words=words
		
	def __call__(self):
		return choice(self.words)
		
first_ball = MysticBall('Да', 'Нет', 'Наверное','Никак нет')
print(first_ball())
print(first_ball())
print(first_ball())
			

			
				