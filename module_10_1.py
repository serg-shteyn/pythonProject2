import threading
from time import sleep,time
from random import randint


words_list='потоковая запись вызов функции итераторы генераторы декораторы ошибки строки список словарь кортеж числа множества классы цикл условие потоки'

def words(count):
	list_=words_list.split(' ')
	for i in range(count):
		yield list_[randint(0,len(list_)-1)]


def write_words(word_count, file_name):
	file_name+='.txt'
	with open(file_name,"w")as file:
		for i in range(1,word_count+1):
			file.write(f"{list(words(220))[i]} ¦ {i}\n")
			sleep(0.05)	
		print(f'Завершилась запись в файл {file_name}')

start_time=time()			
write_words(10,'example1')
write_words(30,'example2')
write_words(200,'example3')
write_words(100,'example4')
end_time=time()
t=round(end_time-start_time,3)
print(f"Время выполнения: {t}с.")

#Создаем потоки
thread1=threading.Thread(target=write_words,args=(10,'example5'))
thread2=threading.Thread(target=write_words,args=(30,'example6'))
thread3=threading.Thread(target=write_words,args=(200,'example7'))
thread4=threading.Thread(target=write_words,args=(100,'example8'))

#Запускаем потоки, фиксируем время начала и конца работы потоков
start_time=time()	
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread1.join()
thread2.join()
thread3.join()
thread4.join()
end_time=time()

t1=round(end_time-start_time,3)
print(f"Время выполнения: {t1}с.")

