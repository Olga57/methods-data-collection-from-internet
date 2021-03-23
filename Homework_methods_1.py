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

url = 'https://samples.openweathermap.org/data/2.5/weather'
appid = '3d3c80fe9fc6fabc5c6777c6e1ece035'
r = requests.get(f'https://samples.openweathermap.org/data/2.5/weather?q=London&appid={appid}')

print (r.text)

print ("Done")

with open('data2.json','w') as f:
    json.dump(r.json(), f)

## Дополнительно выполнила, чтобы разобраться. Непонятно, как token получить. API key как применяется? API key получила на сайте, зарегистрировавшись.
url = 'https://cloud.google.com/maps-platform'
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
}
appid = 'AIzaSyB-urmY7BdS6UlwgF8QplvL8GJOz_DSTbc'
r = requests.get(f'https://cloud.google.com/maps-platform',headers=headers)
from pprint import pprint
pprint(dict(r.headers))
print(r.text)

print ("Done")
print(r.request.headers)