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
        for g in guests:
            for t in self.tables:
                #print(f"t.guest -> {t.guest}")
                if t.guest is None:
                    t.guest = g.name
                    print(f"{g.name} сел(-а) за стол номер {t.number}.")
                    g.start()
                    break
            if not g.is_alive():
            	self.queue.put(g.name)
            	print(f"{g.name} в очереди")

    def discuss_guests(self): # обслужить гостей
        while not self.queue.empty() or not None in self.tables:
        	for t in self.tables:
        		if t.guest is not None and not Guest(name=t.guest).is_alive():
        			print(f'{t.guest} покушал(-а) и ушёл(ушла) и Стол номер {t.number} свободен')
        			t.guest=None
        		if not self.queue.empty() and t.guest == None:
        			t.guest=self.queue.get()
        			print(f"{self.queue.get()} вышел(-ла) из очереди и сел(-а) за стол номер {t.number}")
        			Guest(name=t.guest).start()
        			
        			
        			
        			


# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()