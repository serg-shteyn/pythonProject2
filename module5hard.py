# Классы и объекты."
import time


class User:
	def __init__(self,nik,password,age):
		self.nickname=nik
		self.password=hash(password)
		self.age=age

	def __str__(self):
		return self.nickname
	
	
class Video:
	
	def __init__(self,title,duration,time_now=0,adult_mode=False):
		self.title=title
		self.duration=duration
		self.time_now=time_now
		self.adult_mode=adult_mode

	def __contains__(self, title):
		return title in self.title

	
class UrTube:
	users=[]
	videos=[]
	current_user=None


	def register(self,nickname,password,age):
		check=False
		for i in self.users:
			if i.nickname==nickname:
				check=True
				break
		if not check:
			self.users.append(User(nickname,password,age))
			self.log_in(nickname,password)
		else:
			print(f"Пользователь {nickname} уже существует!")
		
	def log_in(self,nickname,password):
		for i in self.users:
			if (i.nickname == nickname) and (i.password == hash(password)):
				self.current_user=i
				#print(f"Приветствую {self.current_user.nickname}!")
				break

	def log_out(self):
		self.current_user=None
		print('До свидания!')
		
	def get_videos(self,search):
		result=[]
		for i in self.videos:
			if search.lower() in i.title.lower():
				result.append(i.title)
		return result
		
	def add(self, *args):
		for i in args:
			self.videos.append(i)
		
	def watch_video(self,title_film,time_watch=20):
		if self.current_user==None:
			print('Войдите в аккаунт, чтобы смотреть видео')
		else:
			for j in self.videos:
				if title_film in j :
					if (j.adult_mode==True) and (self.current_user.age < 18):
						print('Вам нет 18 лет, пожалуйста покиньте страницу')
						break
					else:
						print(f"Идет просмотр фильма, {title_film}")
						stop_watch = j.time_now + time_watch
						for i in range(j.time_now+1,j.duration+1):
							time.sleep(1)
							j.time_now=i
							print(j.time_now)
							if j.time_now==j.duration:
								print('Конец видео')
								j.time_now=0
							elif j.time_now==stop_watch:
								print(f'Просмотр остановлен на {j.time_now} секунде')
								break

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')



