FROM python
WORKDIR /tests_project/
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV ENV=dev
CMD python -m pytest -s --alluredir=allure_results/ /tests_project/tests/

#docker build -t api_tests .
#docker run --rm --mount type=bind,src=/home/vladimir/PycharmProjects/LearnQA_Python_API,target=/tests_project/ api_tests