# 1. Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя,
# сохранить JSON-вывод в файле *.json.

import json
import requests
import os
from pprint import pprint

username = 'naiteria'

# вариант с авторизацией

# token = os.environ.get('token_github')
# r = requests.get(f'https://api.github.com/users/{username}/repos', auth=(username, token))
# pprint(r.text)

# вариант без авторизации

url = f'https://api.github.com/users/{username}/repos'
user_data = requests.get(url).json()
with open('data.json', 'w') as outfile:
    # json.dump(client.request.host, outfile)
    # json.dump(client.request.headers, outfile)
    json.dump(user_data, outfile, indent=4)

# 2. Изучить    список    открытых    API(https: // www.programmableweb.com / category / all / apis).Найти
# среди    них    любое, требующее    авторизацию (любого    типа).Выполнить    запросы    к
# нему, пройдя    авторизацию. Ответ    сервера    записать    в    файл.    Если    нет
# желания    заморачиваться    с    поиском, возьмите    API    вконтакте (https: // vk.com / dev / first_guide).
# Сделайте запрос, чтобы    получить    список    всех    сообществ    на    которые    вы    подписаны.


user_id = input('Введите id пользователя или его user_name:')
# user_id = 'naiteria'


url = 'https://api.vk.com/method/groups.get'
token = 'token_vk_api'
params = {
    'v': 5.131,
    'access_token': token
}
req = requests.get(url, params=params)

if req.ok:
    data = req.json()
    response_file = open('data_vk.json', 'w', encoding="utf-8")
    response_file.write(f'{data} \n')
    response_file.close()
    print(f'{data} \n')
else:
    print('Проверьте разрешения и срок действия токена')

