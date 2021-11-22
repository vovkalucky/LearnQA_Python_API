# Ex6: Длинный редирект
# Необходимо написать скрипт, который создает GET-запрос на метод: https://playground.learnqa.ru/api/long_redirect
# С помощью конструкции response.history необходимо узнать, сколько редиректов происходит от изначальной точки н
# азначения до итоговой. И какой URL итоговый.
# Ответ опубликуйте в виде ссылки на коммит со скриптом, а также укажите количество редиректов и конечный URL.
import requests
res = requests.get('https://playground.learnqa.ru/api/long_redirect')
for site in res.history:
    print(site.url)
print(f'Count of redirects: {len(res.history)}, End URL: {res.history[-1].url}')