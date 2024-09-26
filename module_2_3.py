#Стиль кода часть II. Цикл While

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
len_=len(my_list)
a=0
while my_list[a] > 0 or my_list[a]==0:
	if my_list[a]==0:
		a+=1
		if a == len_:
		        break
		continue
	else :
	    print(my_list[a])
	    a += 1
	    if a == len_:
		    break
		