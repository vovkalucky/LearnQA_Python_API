import requests
res= requests.get('https://playground.learnqa.ru/api/get_301', allow_redirects=False)
print(res.status_code)
print(res.headers)
