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
	
	def __init__(self):
		self.data = {}
		
	def add_user(self,username,password):
		self.data[username]=password
		
	def register(self,login,password):
		if login in self.data:
			print('ok')
		else:
			print('no')
		
if __name__=="__main__":
		database=Database()
while True:
		choise = input('Приветствую! Выберите действие: \n1 - Вход \n2 -  Регистрация \n')
		if choise=="2":
			user=User(input("Введите логин: "),password := input('Введите пароль: '),password2 := input('Повторите пароль: '))
			if password != password2:
				exit()
			database.add_user(user.username,user.password)
		elif choise=='1':
			database.register(input('Введите логин: '),input('Введите пароль: '))
			
		
		
		
		print(database.data)
		
		
