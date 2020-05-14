""""
 1. Посмотреть документацию к API GitHub,
разобраться как вывести список репозиториев для конкретного пользователя,
сохранить JSON-вывод в файле *.json.
"""
import requests
import json

username = input('Введите username:  ')
main_link = f'https://api.github.com/users/{username}/repos'
response = requests.get(main_link)

if response.ok:
    data = json.loads(response.text)

with open('response_file.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=2, ensure_ascii=False)



# 2. Изучить список открытых API.
# Найти среди них любое, требующее авторизацию (любого типа).
#  Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл.

api_url = "http://api.captchatronix.com/"
api_username = "igormir"
api_password = "12345678"


# FUNCTION TO CHECK INTEGRATION (function=balance)
def get_balance():
    global api_url, api_username, api_password;

    data = {"function": "balance",
            "username": api_username,
            "password": api_password}

    request = requests.post(api_url, data)

    return request.content

# USAGE OF THE FUNCTION
balance = get_balance()
print(balance)