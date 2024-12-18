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
                if t.guest is None:
                    t.guest = g
                    print(f"{g.name} сел(-а) за стол номер {t.number}.")
                    g.start()
                    break
                else:
                    self.queue.put(g)
                    print(f"{g.name} в очереди")







    def discuss_guests(self): # обслужить гостей
        pass


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










def getter(queue):
    while True:
        time.sleep(4)
        item = queue.get()
        print(threading.current_thread(), 'Взят элемент',item)


q = Queue()
thread1 = threading.Thread(target=getter,args=(q,),daemon=True)
#thread1.start()

#for i in range(10):
#    time.sleep(2)
#    q.put(i)
#   print(threading.current_thread(), 'Положил в очередь элемент,', i)


