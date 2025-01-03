import requests
import time
from PIL import Image
import os
import pandas as pd
import openpyxl


#Работа с request
r=requests.get('https://github.com')
#выводим статус подключения
print(f"Статус подключения: {r.status_code}")

#выводим заголовки сайта
count=1
for i,v in r.headers.items():
	time.sleep(0.2)
	print(i,'->',v)
	count+=1
	if count>5:
		break
		
# pillow
#открываем изображение
image=Image.open('img_2025.jpg')
#обрезаем изображение
cropped=image.crop((0,0,800,200))
#сохраняем обрезанное изображение
cropped.save(os.path.join(os.getcwd(),'img_2025_small.jpg'))

#pandas
#Создание датафрейма вручную
df=pd.DataFrame([[1,'a',3,4,5,6,7],[2,'b',13,14,15,16,17],[3,'c',18,19,20,21,22]],columns=['id','A','B','C','D','E','F'])
#Сохраняем в файл csv
df.to_csv('save_csv.csv',index=False)
#Сохраняем в excel
df.to_excel('save_exel.xlsx',index=False)



