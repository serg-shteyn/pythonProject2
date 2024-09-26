# Неизменяемые и изменяемые объекты

immutable_var=('apple',True,233,15,[3,7,9,1],False)
print('кортеж:',immutable_var)
# immutable_var[0]='orange' 
# Кортеж не поддерживает обращение по эллементам.

mutable_list=[2,7,15,'book','home']
mutable_list[0]='dog'
print('список:',
mutable_list)