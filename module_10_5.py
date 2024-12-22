# Многопроцессное программирование
#Цель: понять разницу между линейным и многопроцессным подходом, выполнив операции обоими способами.

import time
from multiprocessing import Pool

def read_info(name):
	all_data=[]
	with open(name,'r') as file:
		while True:
			line=file.readline()
			if line:
				all_data.append(line)
			else:
				break
		
		
file_list=[f'./file {x}.txt' for x in range(1,5)]

# Линейный вызов
print('Линейный вызов...')
start=time.time()

list(map(read_info, file_list))

end=time.time()
t1=round(end-start,5)

print(f'Линейный вызов закончен: {t1}')


# Многопроцессорный вызов	
print()
print('Многопроцессорный вызов...')
start=time.time()	
if __name__ == '__main__':
    with Pool(4) as p:
    	p.map(read_info, file_list)

end=time.time()
t2=round(end-start,6)

print(f'Многопроцессорный вызов закончен: {t2}')

t3=round(t1/t2,1)
print()
print(f'Многопроцессорный режим быстрее линейного в {t3} раз')