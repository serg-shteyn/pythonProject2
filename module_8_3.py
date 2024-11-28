# Создание исключений

class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

class Car:
    

    def __init__(self,model,vin,numbers):
        self.__is_valid_vin(vin)
        self.__is_valid_numbers(numbers)
        self.model = model
        self.__vin = vin
        self.__numbers = numbers

    def __is_valid_vin(self,vin_number):
        if  not isinstance(vin_number,int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        elif vin_number < 1000000 or vin_number > 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            return True

    def __is_valid_numbers(self,num):
        if not isinstance(num,str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(num) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        else:
            return True


try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')