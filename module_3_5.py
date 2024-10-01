# Рекурсия

def get_multiplied_digits (number):
	str_number = str(number)
	first = int(str_number[0])
	if len(str_number)>1:
		return (first *    get_multiplied_digits(int(str_number[1:])))
	else:	# удаление нуля, если он последний
		if first != 0: 
		    return first
		else:
			return True

	
result = get_multiplied_digits(40030)
print(result)
