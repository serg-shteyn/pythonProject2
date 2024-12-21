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
    
    #наличие хотябы одного пустого стола
    def table_free(self): 
    	for t in self.tables:
    		if t.guest is None:
    		    return True
    	return False
    
    #наличие хотябы одного занятого стола,  any работает также, но у меня его не получилось применить any(self.table) работает не также почему-то
    def table_notfree(self):
    	for t in self.tables:
    		if t.guest is not None:
    			return True
    	return False

    # прибытие гостей
    def guest_arrival(self, *guests):
        for g in guests:
            if not self.table_free():
            	self.queue.put(g)
            	print(f"{g.name} в очереди")
            else:
                for t in self.tables:
                	if t.guest is None:
                	   t.guest = g
                	   print(f"{g.name} сел(-а) за стол номер {t.number}.")
                	   g.start()
                	   break

    def discuss_guests(self): # обслужить гостей
        while not self.queue.empty() or self.table_notfree():
        	for t in self.tables:
        		if t.guest is not None and not t.guest.is_alive():
        			print(f'{t.guest.name} покушал(-а) и ушёл(ушла) и Стол номер {t.number} свободен')
        			t.guest=None
        		if not self.queue.empty() and t.guest is None:
        			t.guest=self.queue.get()
        			print(f"{t.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {t.number}")
        			t.guest.start()
        		
        print('Все гости обслужены и в очереди никого нет.')
        			

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