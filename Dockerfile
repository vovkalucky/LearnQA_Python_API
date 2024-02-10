FROM python
WORKDIR /tests/
COPY requirements.txt .
RUN pip install -r requirements.txt
# Создаем непривилегированного пользователя
RUN useradd -m myuser
# Меняем владельца рабочей директории
RUN chown -R myuser:myuser /tests
# Переключаемся на непривилегированного пользователя
USER myuser

ENV ENV=dev
CMD python -m pytest -s --alluredir=allure_results/ /tests/

#docker build -t api_tests_1002 .
#docker run --rm --mount type=bind,src=/home/vladimir/PycharmProjects/LearnQA_Python_API,target=/tests api_tests_1002