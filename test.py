import random

secret = random.randint(1,101)
my_i=0
tr=0
while secret!=my_i:
    my_i=int(input('Введите число: '))
    tr += 1
    if secret < my_i:
        print("меньше")
    elif secret > my_i:
        print("больше")
    else:
        print (f"Вы угадали! Секретное число {secret}, за {tr} попыток")
