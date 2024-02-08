import pytest
import allure
from lib.assertions import Assertions
from lib.my_requests import MyRequests


email_negative_login = [
    pytest.param(('vinkotov123@example.com', '1234'), id="vinkotov123@example.com, 1234"),
    pytest.param(('vinkotov123@example.com', ''), id='vinkotov123@example.com, empty password'),
    pytest.param(('123@example.com', '123'), id='123@example.com, 123')
    ]

email_positive_login = [
    pytest.param(('vinkotov@example.com', '1234'), id='vinkotov@example.com, 1234'),
    pytest.param(('learnqa02072024222439@example.com', '123'), id='learnqa02072024222439@example.com, 123')
    ]


@pytest.mark.parametrize('data', email_positive_login)
@allure.title("This test successfully login user into the system")
def test_positive_login_user(data):
    email, password = data
    response = MyRequests.post("/user/login", data={"email": email, "password": password})
    Assertions.assert_code_status(response,200)


@pytest.mark.parametrize('data', email_negative_login)
@allure.title("This test NOT login user into the system")
def test_negative_login_user(data):
    email, password = data
    response = MyRequests.post("/user/login", data={"email": email, "password": password})
    Assertions.assert_code_status(response,400)