# Декораторы
# Цель задания:
# Освоить механизмы создания декораторов Python.
# Практически применить знания, создав функцию декоратор и обернув ею другую функцию.

def is_prime(func):
	def wraper(a,b,c):
		sum_=func(a,b,c)
		# 1 не составное и не простое
		if sum_==1:
			return sum_
		for i in range(2,sum_):
			#если 2, печатаем простое
			if not sum_%i and sum!=2:
				print('Составное')
				return sum_
		print('Простое')
		return sum_
	return wraper

@is_prime
def sum_three(a,b,c):
	return a+b+c
	
result = sum_three(1,9,2)
print(result)
	