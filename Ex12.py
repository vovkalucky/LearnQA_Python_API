# Ex12: Тест запроса на метод header
#
# Необходимо написать тест, который делает запрос на метод: https://playground.learnqa.ru/api/homework_header
# Этот метод возвращает headers с каким-то значением. Необходимо с помощью функции print()
# понять что за headers и с каким значением, и зафиксировать это поведение с помощью assert
#
# Чтобы pytest не игнорировал print() необходимо использовать ключик "-s": python -m pytest -s my_test.py
import requests
class TestApi:
    def test_api(self):
        url = 'https://playground.learnqa.ru/api/homework_header'
        response = requests.get(url)
        print(response.headers)
        secret_key = 'x-secret-homework-header'
        assert secret_key in response.headers, f'{secret_key} not in headers!'
        assert response.headers[secret_key] == "Some secret value", 'Not correct value!'
