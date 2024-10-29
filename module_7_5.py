# Файлы в операционной системе

import os
import time
pathpy='/storage/emulated/0/qpython'
target='urban'
directory = os.path.join(pathpy,target)

for root,dirs,files in os.walk(directory):
	for file in files:
		filepath=os.path.join(root,file)
		filesize=os.path.getsize(filepath)
		parent_dir=os.path.dirname(filepath)
		filetime=os.path.getmtime(filepath)
		formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
		
		print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
		print('—'*30)
	