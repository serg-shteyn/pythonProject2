# Классы и объекты."

class User:
	def __init__(self,nik,password,age):
		self.nikname=nik
		self.password=hash(password)
		self.age=age
	
	
class Video:
	
	def __init__(self,title,duration,time_now=0,adult_mode=False):
		self.title=title
		self.duration=duration
		self.time_now=time_now
		self.adult_mode=adult_mode
	
class UrTube:
	users=[]
	videos=[]
	current_user=None
	
	def register(self):
		pass
		
	def login(self):
		pass
		
	def get_videos(self,search):
		pass
		
	def add(self, *args):
		for i in args:
			self.videos.append(i)
		
	def watch_video(self):
		pass
		
	
	
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)	
maks=User('maksim','2233',5)
print(maks.password)
ur=UrTube()
ur.users.append(maks)
print(ur.users)
ur.add(v1,v2)
print(ur.videos)

