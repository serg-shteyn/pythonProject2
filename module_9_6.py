# Генераторы
#Цель: более глубоко понять особенности работы с функциями генераторами и оператором yield в Python.

from itertools import combinations

def all_variants(text):
	for var in range(1,len(text)+1):
		for result in combinations(text,var):
			str=''
			for n in result:
				str+=n
			yield str
			
		
a = all_variants("abc")
for i in a:
	print(i)