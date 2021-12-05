import json
from requests import Response

class BaseCase:
    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"Can not find cookie in {cookie_name} in the last response"
        return response.cookies[cookie_name]

    def get_header(self, response: Response, headers_name):
        assert headers_name in response.headers, f"Can not find header with the name {headers_name} in the response"
        return response.headers[headers_name]

    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecoderError:
            assert False, f"response is not in JSON format"
        assert name in response_as_dict, f"Response JSON does not have key {name}"
        return response_as_dict[name]