import requests
payload = {'login':'secret_login', 'password':'secret_pass'}
res = requests.post('https://playground.learnqa.ru/api/get_auth_cookie', data=payload)
# print(res.text)
# print(res.status_code)
# print(dict(res.cookies))
cookie_value = res.cookies.get('auth_cookie')
cookie = {}
if cookie_value is not None:
    cookie.update({'auth_cookie' : cookie_value})
res2 = requests.post('https://playground.learnqa.ru/api/check_auth_cookie', cookies=cookie)
print(res2.text)