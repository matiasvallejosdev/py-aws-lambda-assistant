import pytest

from lambda_assistant.response.headers import CORSHeaders
from lambda_assistant.errors import *

class TestResponseBuilder:

    @pytest.mark.parametrize(
        'credentials, expected',
        [
            (
                True,
                {
                    'Access-Control-Allow-Credentials': True,
                    'Access-Control-Allow-Origin': '*',
                    'Content-Type': 'application/json'
                }           
            ),
            (
                False,
                {
                    'Access-Control-Allow-Origin': '*',
                    'Content-Type': 'application/json'
                }           
            )
        ],
    )
    def test_build_headers(self, credentials, expected):
        obj = CORSHeaders('*', credentials)
        headers = obj.buildHeaders()
        
        assert headers == expected
        
    def test_build_class(self):
        obj = CORSHeaders()  
        assert obj.origin == '*'
        assert obj.credentials == False
        
        obj = CORSHeaders('localhost', True)  
        assert obj.origin == 'localhost'
        assert obj.credentials == True