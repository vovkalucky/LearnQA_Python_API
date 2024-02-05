# Ex7: Запросы и методы
#
# Сегодня задача должна быть попроще. У нас есть вот такой URL: https://playground.learnqa.ru/ajax/api/compare_query_type
# Запрашивать его можно четырьмя разными HTTP-методами: POST, GET, PUT, DELETE

# При этом в запросе должен быть параметр method. Он должен содержать указание метода, с помощью которого вы делаете запрос.
# Например, если вы делаете GET-запрос, параметр method должен равняться строке ‘GET’. Если POST-запросом -
# то параметр method должен равняться ‘POST’. И так далее.
#
# Надо написать скрипт, который делает следующее:
#
# 1. Делает http-запрос любого типа без параметра method, описать что будет выводиться в этом случае.
# 2. Делает http-запрос не из списка. Например, HEAD. Описать что будет выводиться в этом случае.
# 3. Делает запрос с правильным значением method. Описать что будет выводиться в этом случае.
# 4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method.
# Например с GET-запросом передает значения параметра method равное ‘GET’, затем ‘POST’, ‘PUT’, ‘DELETE’ и так далее.
# И так для всех типов запроса. Найти такое сочетание, когда реальный тип запроса не совпадает со значением параметра,
# но сервер отвечает так, словно все ок. Или же наоборот, когда типы совпадают, но сервер считает, что это не так.
#
# Не забывайте, что для GET-запроса данные надо передавать через params=
# А для всех остальных через data=
#

#1
import requests
res = requests.get('https://playground.learnqa.ru/ajax/api/compare_query_type')
print(res.text)
#2
params = {'method':'HEAD'}
res2 = requests.get('https://playground.learnqa.ru/ajax/api/compare_query_type', params=params)
print(res2.text)
#3
params = {'method':'GET'}
res3 = requests.get('https://playground.learnqa.ru/ajax/api/compare_query_type', params=params)
print(res3.text)
#4
print('----GET----')
methods =['GET','POST','PUT','DELETE']
for m in methods:
    params = {'method' : m}
    res3 = requests.get('https://playground.learnqa.ru/ajax/api/compare_query_type', params=params)
    print(res3.text)
print('----POST----')
for m in methods:
    params = {'method' : m}
    res4 = requests.post('https://playground.learnqa.ru/ajax/api/compare_query_type', data=params)
    print(res4.text)
print('----PUT----')
for m in methods:
    params = {'method' : m}
    res5 = requests.put('https://playground.learnqa.ru/ajax/api/compare_query_type', data=params)
    print(res5.text)
print('----DELETE----')
for m in methods:
    params = {'method' : m}
    res6 = requests.delete('https://playground.learnqa.ru/ajax/api/compare_query_type', data=params)
    print(res6.text)
