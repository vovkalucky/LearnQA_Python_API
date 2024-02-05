import pytest
import allure
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests


@allure.feature("Check Authorization")
class TestUserAuth(BaseCase):
    exclude_params = [
        ("no_cookie"),
        ("no_token")
    ]

    @pytest.fixture(autouse=True)
    def setup_auth(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = MyRequests.post("/user/login", data=data)
        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")

        return {
            "auth_sid": auth_sid,
            "token": token,
            "user_id_from_auth_method": user_id_from_auth_method
        }

    @allure.title("This test successfully authorization by email and password")
    def test_auth_user(self, setup_auth):
        response2 = MyRequests.get("/user/auth",
                                   headers={"x-csrf-token": setup_auth["token"]},
                                   cookies={"auth_sid": setup_auth["auth_sid"]}
                                  )
        Assertions.assert_json_value_by_name(
            response2,
            "user_id",
            setup_auth["user_id_from_auth_method"],
            "User id from auth method is not equal to user id from check method"
        )

    @allure.title("This test checks authorization status without cookie or token")
    @pytest.mark.parametrize('condition', exclude_params)
    def test_negative_auth_check(self, setup_auth, condition):
        if condition == 'no_cookie':
            response2 = MyRequests.get(
                '/user/auth',
                headers={"x-csrf-token": setup_auth["token"]}
            )
        elif condition == 'no_token':
            response2 = MyRequests.get(
                '/user/auth',
                cookies={"auth_sid": setup_auth["auth_sid"]}
            )

        Assertions.assert_json_value_by_name(
            response2,
            "user_id",
            0,
            f"User is authorized with condition {condition}"
        )
