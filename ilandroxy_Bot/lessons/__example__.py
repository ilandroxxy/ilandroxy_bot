
'''
import requests

url = 'https://wttr.in'  # не изменяйте значение URL

weather_parameters = {
    '0': '',
    'T': '',
    'M': '',
    'lang': 'ru'
    # добавьте параметр запроса `T`, чтобы вернулся чёрно-белый текст
}

response = requests.get(url, params=weather_parameters)  # передайте параметры в http-запрос
print(response.text)
'''

'''
import requests

url = 'https://wttr.in'

weather_parameters = {
    '0': '',
    'T': '',
    'M': '',

}

request_headers = {
    'Accept-Language': 'ru'# заполните словарь с заголовками
}

# не забудьте передать параметры и заголовки в http-запрос
# через аргументы `params` и `headers` функции get()
response = requests.get(url, params = weather_parameters,headers=request_headers)
print(response.text)
'''
while True:
    print("case 1: Введите два катита\ncase 2: Введите катет и гипотенузу\ncase 0: exit\ncase = ")
    case = int(input())
    if case == 1:
        print('Введите два катита: ')
        a = int(input())
        b = int(input())
        c = (a ** 2 + b ** 2) ** (1/2)
        print(f'Гипотенуза = {c}')
    elif case == 2:
        print("Введите катет")
        a = int(input())
        print("Введите гипотенузу")
        c = int(input())
        b = (c ** 2 - a ** 2) ** (1 / 2)
        print('Катет =', b)
    elif case == 0:
        break