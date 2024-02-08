import pytest
import allure
from lib.assertions import Assertions
from lib.my_requests import MyRequests
from lib.base_case import BaseCase


@allure.title("This test check delete user from the system")
def test_delete_user():
    reg_data = BaseCase()
    register_data = reg_data.prepare_registration_data()
    print(register_data)
    user_email = register_data["email"]
    user_password = register_data["password"]
    with allure.step('User create'):
        response = MyRequests.post("/user/", data=register_data)
        Assertions.assert_code_status(response,200)
    with allure.step('User login'):
        response = MyRequests.post("/user/login", data={"email": user_email, "password": user_password})
        Assertions.assert_json_has_key(response, "user_id")
        user_id = response.json()["user_id"]
    auth_sid = reg_data.get_cookie(response, 'auth_sid')
    token = reg_data.get_header(response, 'x-csrf-token')
    with allure.step('Delete user'):
        response = MyRequests.delete(f"/user/{user_id}", headers={'x-csrf-token': token}, cookies={'auth_sid': auth_sid})
        Assertions.assert_code_status(response, 200)
    with allure.step('Check delete user id'):
        response = MyRequests.get(f"/user/{user_id}")
        Assertions.assert_code_status(response, 404)
