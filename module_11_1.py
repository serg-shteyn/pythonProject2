import requests
import time
from PIL import Image
import os


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


