# Ex10: Тест на короткую фразу
#
# В рамках этой задачи с помощью pytest необходимо написать тест, который просит ввести в консоли любую фразу короче 15 символов. А затем с помощью assert проверяет, что фраза действительно короче 15 символов.
#
# Чтобы в переменную получить значение, введенное из консоли, необходимо написать вот такой код:
# phrase = input("Set a phrase: ")
#
# Внимание, чтобы pytest не игнорировал команду ввода с клавиатуры, запускать тест нужно с ключиком "-s": python -m pytest -s my_test.py

class TestPhrase:
    def test_length_of_phrase(self):
        phrase = input("Set a phrase: ")
        assert len(phrase) < 15, 'Length of phrase >= 15'
    def test_length_of_phrase2(self):
        phrase = input("Set a phrase: ")
        assert len(phrase) == 15, 'Length of phrase != 15'