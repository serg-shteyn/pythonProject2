# Блокировки и обработка ошибок
# Цель: освоить блокировки потоков, используя объекты класса Lock и его методы.
from random import randint
import threading
import time

class Bank:
	
	def __init__(self):
		self.balance=0
		self.lock=threading.Lock()
		
	def deposit(self):
		for i in range(100):
			put=randint(50,500)
			if self.balance >=500 and self.lock.locked():
				self.lock.release()
			self.balance+=put
			print(f"Пополнение: {put}. Баланс: {self.balance}")
			time.sleep(0.001)
			
	def take(self):
		for i in range(100):
			take=randint(50,500)
			print(f"Запрос на {take}.")
			if take<=self.balance:
				self.balance-=take
				print(f"Снятие: {take}. Баланс: {self.balance}")
			else:
				print(f"Запрос отклонён, недостаточно средств")
				self.lock.acquire()
			time.sleep(0.001)
				
		
bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
		