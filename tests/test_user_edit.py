import requests

from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests
import allure


@allure.feature("Edit user cases")
class TestUserEdit(BaseCase):
    @allure.title('Check edit created user')
    def test_edit_created_user(self):
        #REGISTER
        register_data = self.prepare_registration_data()
        response_reg = MyRequests.post('/user/', data=register_data)
        Assertions.assert_code_status(response_reg, 200)
        Assertions.assert_json_has_key(response_reg, 'id')
        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response_reg, 'id')

        #LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response_login = MyRequests.post('/user/login', data=login_data)
        auth_sid = self.get_cookie(response_login, 'auth_sid')
        token = self.get_header(response_login, 'x-csrf-token')
        #EDIT
        new_name ='vladislav43804580608'

        response_edit = MyRequests.put(f'/user/{user_id}',
                                 headers={'Content-Type': 'application/json',
                                          'x-csrf-token': token},
                                 cookies={'auth_sid': auth_sid},
                                 data={
                                     "firstName": new_name
                                     #"email": "dsff@ddsfddsfd.ru",
                                     #"password": "qwerty"
                                 }
                                       )
        Assertions.assert_code_status(response_edit, 200)

        #AUTH
        response_auth = MyRequests.get(f'/user/auth',
                                       headers={'x-csrf-token': token},
                                       cookies={'auth_sid': auth_sid})

        #GET
        response_get = MyRequests.get(f'/user/{user_id}',
                                      headers={'x-csrf-token': token},
                                      cookies={'auth_sid': auth_sid})
        Assertions.assert_json_value_by_name(
            response_get,
            'firstName',
            new_name,
            "Wrong name of the user after edit"
        )
