# Дополнительное практическое задание по модулю: "Наследование классов."
import math

class Figure:
	sides_count=0
	filled = True
	
	def __init__(self,color,*sides):
		self.__sides = None
		if self.__is_valid_color(color):
			self.__color=color

		
	def get_color(self):
		return self.__color
		
	def __is_valid_color(self,*color):
		for i in color:
			if isinstance(i,int) and i>=0 and i<=255 :
				pass	
			else:
				return False
			return True
			
	def set_color(self,r,g,b):
		if self.__is_valid_color(r,g,b):
			self.__color=r,g,b


	def get_sides(self):
		print(self.__sides)


class Circle(Figure):

	def check_sides(self,*new_sides):
		return True

	def set_sides(self,*new_sides):
		if self.check_sides(new_sides):
			self.__sides = new_sides



class Cube(Figure):
	pass




circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
#cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
#cube1.set_color(300, 70, 15) # Не изменится
#print(cube1.get_color())

# Проверка на изменение сторон:
#cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
#print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())
