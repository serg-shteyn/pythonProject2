# Дополнительное практическое задание по модулю: "Наследование классов."
import math

class Figure:
	sides_count=0
	filled = True
	__color=(0,0,0)
	__sides=0
	
	def __init__(self,color,*sides):
		if self.__is_valid_color(color):
			self.__color=color
		
	def get_color(self):
		return self.__color
		
	def __is_valid_color(self,color):
		for i in color:
			if isinstance(i,int) and i>=0 and i<=255 :
				pass	
			else:
				return False
		if len(color)==3:
		    return True
			
	def set_color(self,*color):
		if self.__is_valid_color(color):
			self.__color=color
				
#	def set_sides(self,*new_sides):
#		if len(new_sides)==self.sides_count:
#			self.__sides=new_sides
			
	def get_sides(self):
		return self.__sides
			
				
class Circle(Figure):	
	sides_count=1
	
	def __init__(self,color,*sides):
		super().__init__(color,sides)
		self.set_sides(sides)
		#self.__radius = self.get_radius(self.get_sides())
		
	def set_sides(self,new_sides):
		print('₽',new_sides)
		if len(new_sides)!=self.sides_count:
			self.__sides=1
		else:
			self.__sides=new_sides
		
	def get_radius(self,side):
		return side[0]/(2*math.pi)
	
	def get_square(self):
		return math.pi*(self.get_radius(self.get_sides())**2)
		
		
class Cube(Figure):
	pass
		
circle1 = Circle((200, 200,200), 10,23) # (Цвет, стороны)
print("f",circle1.get_sides())
#cube1 = Cube((222, 35, 130), 6)
print(circle1.get_color())
# Проверка на изменение цветов:
circle1.set_color(55,45, 77) # Изменится
print(circle1.get_color())
#cube1.set_color(300, 70, 15) # Не изменится
#print(cube1.get_color())

# Проверка на изменение сторон:
#cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
#print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())