# Различие атрибутов класса 

class House:
    houses_history = []

    def __new__(cls, name,floor):
        obj = super().__new__(cls)
        obj.houses_history.append(name)
        return obj

    def __init__(self, name, floor):
        self.name = name
        self.number_of_floors = floor
  
    def __del__(self):
     	print (f"{self.name}снесён, но он останется в истории")

    def other_check(self, other):
        if isinstance(other, int):
            return other
        elif isinstance(other, House):
            return other.number_of_floors
        elif isinstance(other, str):
            return int(other)

    def __len__(self):
        return self.number_of_floors

    def __lt__(self, other):  # <
        return self.number_of_floors < self.other_check(other)

    def __le__(self, other):  # <=
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):  # >
        return not self.__le__(other)

    def __ge__(self, other):  # >=
        return not self.__lt__(other)

    def __eq__(self, other):  # ==
        return self.number_of_floors == self.other_check(other)

    def __ne__(self, other):  # !=
        return not self.__eq__(other)

    def __add__(self, value):
        self.number_of_floors = self.number_of_floors + self.other_check(value)
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    def __str__(self):
        return (f"Название: {self.name}, кол-во этажей: {self.number_of_floors}")

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует.")
        else:
            for i in range(1, new_floor + 1):
                print(i)



h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)