### Задание 1
### Посмотреть документацию к API GitHub,
### разобраться как вывести список репозиториев для конкретного пользователя, сохранить JSON-вывод в файле *.json.
import requests
import json
url = 'https://api.github.com/'
user = 'Olga57'

r = requests.get(f'https://api.github.com/users/{user}/repos')
print("Done")


with open('data.json', 'w') as f:
    json.dump(r.json(), f)

for i in r.json():
    print(i['name'])

### 2. Изучить список открытых API. Найти среди них любое,
# требующее авторизацию (любого типа).
# Выполнить запросы к нему, пройдя авторизацию.
# Ответ сервера записать в файл.
appid = '3d3c80fe9fc6fabc5c6777c6e1ece035'
base_url = 'https://api.openweathermap.org/data/2.5/weather'

r2 = requests.get(f'{base_url}?q=Moscow&appid={appid}')

print (r2.text)

print ("Done")

with open('data1.json', 'w') as f:
    json.dump(r2.json(), f)
