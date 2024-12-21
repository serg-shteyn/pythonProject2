# Очереди для обмена данными между потоками.
# Задача "Потоки гостей в кафе":

from queue import Queue
import time
import random
import threading

class Table:
    def __init__(self,num,guest=None):
        self.number = num
        self.guest = guest

class Guest(threading.Thread):
    def __init__(self,name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(random.randint(3,10))

class Cafe:
    def __init__(self,*tabl):
        self.tables = tabl
        self.queue = Queue()

    # прибытие гостей
    def guest_arrival(self, *guests):
        #Принимаем гостей по очереди
        for g in guests:
            #если нет свободного стола
            if all([x.guest for x in self.tables]):
            	self.queue.put(g)
            	print(f"{g.name} в очереди")
            else:
                # ищем свободный стол
                for t in self.tables:
                	#если стол не занят
                	if not t.guest:
                	   #сажаем за стол следующего гостя
                	   t.guest = g
                	   print(f"{g.name} сел(-а) за стол номер {t.number}.")
                	   g.start()
                	   break

    def discuss_guests(self): # обслужить гостей
        while not self.queue.empty() or any([x.guest for x in self.tables]):
        	for t in self.tables:
        		if t.guest and not t.guest.is_alive():
        			print(f'{t.guest.name} покушал(-а) и ушёл(ушла) и Стол номер {t.number} свободен')
        			t.guest=None
        		if not self.queue.empty() and not t.guest:
        			t.guest=self.queue.get()
        			print(f"{t.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {t.number}")
        			t.guest.start()
        		
        print('Все гости обслужены и в очереди никого нет.')
        			

# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra','Vasy','Dima','Svetlana'
]

# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()