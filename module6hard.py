# Дополнительное практическое задание по модулю: "Наследование классов."

class Figure:
	sides_count=0
	
	def __init__(self,sides,color,filled):
		self.__sides=sides
		self.__color=color
		self.filled=filled
		
	def get_color(self):
		return self.color
		
	def is_valid_color(self,r,g,b):
		if type(r)==int and type(g)==int and type(b)==int:
			if r >=0 and r<=255 and g >=0 and g<=255 and b>=0 and b<=255:
				print(True)
				return True
			else:
				print(False,"диапазон 0-255")
				return False
		else:
			print (False, "не целое число")
			return False
			
	def set_color(self,r,g,b):
			if self.is_valid_color(r,g,b):
				self.__color=(r,g,b)
				
	
		
f=Figure((67,5,7),(3,54,89),True)
f.is_valid_color(0,255,0)