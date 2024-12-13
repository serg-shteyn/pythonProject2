# Потоки на классах
from threading import Thread
import time

class Knight(Thread):
	
	def __init__(self,name,power):
		super().__init__()
		self.name=name
		self.power=power
		
	def run(self):
		enemys=100
		days=0
		print(f"{self.name}, на нас напали!")
		while enemys>0:
			time.sleep(1)
			days+=1
			enemys-=self.power
			print(f"{self.name} сражается {days} {self.day(days)}..., осталось {enemys} воинов.")
		print(f"{self.name} одержал победу спустя {days} {self.day(days)}!")
	
	# Правильно печатаем слово день(дней) :-)
	def day(self,day):
		if day>4 and day<20:
			return 'дней'
		day=int(str(day)[-1])
		if day==1:
			return 'день'
		elif day==2 or day==3 or day==4:
			return 'дня'
		else:
			return 'дней'
		
		
		
# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

# Вывод строки об окончании сражения
print('Все битвы закончились!')
