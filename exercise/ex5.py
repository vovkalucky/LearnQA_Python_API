# Наша задача с помощью библиотеки “json”, которую мы показывали на занятии, распарсить нашу переменную
# json_text и вывести текст второго сообщения с помощью функции print.

import json
json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
json_obj = json.loads(json_text)
#print(type(json_obj))
print(json_obj['messages'][1]['message'])

