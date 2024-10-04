# Дополнительное практическое задание по модулю

def calculate_structure_sum(data,sum):
	if isinstance(data,(list,set,tuple)):
		for i in data:
			sum = (calculate_structure_sum(i,sum))
		return sum
	if isinstance(data,dict):
		for key,value in data.items():
			sum=(calculate_structure_sum(key,sum=0))+(calculate_structure_sum(value,sum=0))+sum
		return sum
	elif isinstance(data,(int,float)):
		return data+sum
	elif isinstance(data,str):
		return len(data)+sum

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure,sum=0)
print(result)
