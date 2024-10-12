class User:
	"""
Класс пользователя, содержащий атрибуты: логин, пароль.
	
	"""
	def __init__(self,username,password,password_confirm):
		self.username=username
		if password==password_confirm:
			self.password = password
		
			

print(User.__doc__)

class Database:
	l=''
	def __init__(self):
		self.data = {'serg':'2233','shteyn':'3377'}

		
	def add_user(self,username,password):
		self.data[username]=password
		
	def register(self,login,password):
		if login in self.data:
			if password == self.data[login]:
				self.l=login
				print(f"Приветствую {login}! Вы вошли в свой аккаунт.")
				print()
				print('-'*22)
			else:
				print('Не верный пароль!')
		else:
			print('Такого пользователя нет в списке!!!')
		
if __name__=="__main__":
		database=Database()
while True:
		choise = input(f'Приветствую {database.l}! Выберите действие: \n1 - Вход \n2 -  Регистрация \n3 - Выход \n4 - Список пользователей \n')
		if choise=="2":
			user=User(input("Введите логин: "),password := input('Введите пароль: '),password2 := input('Повторите пароль: '))
			if password != password2:
				print('Пароли не совпадают.')
				continue
			database.add_user(user.username,user.password)
		elif choise=='1':
			database.register(input('Введите логин: '),input('Введите пароль: '))
		elif choise=='4':
			print('-'*22)
			print()
			for i in database.data:
				print(i)
			print()
			print('-' * 22)
		else:
			exit('Выход')
			

