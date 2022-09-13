
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

f = open('24.txt', 'r')
s = f.readline()

count = 1
maxi = 0
for i in range(0, len(s)-1):
    if (s[i] == 'K' and s[i+1] == 'L') or (s[i] == 'L' and s[i+1] == 'K'):
        count = 1
    else:
        count += 1
        if count > maxi:
            maxi = count
print(maxi)

