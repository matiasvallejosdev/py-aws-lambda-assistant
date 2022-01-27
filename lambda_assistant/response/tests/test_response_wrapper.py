import pytest
from http import HTTPStatus

from lambda_assistant.response.wrapper import *
from lambda_assistant.response.headers import CORSHeaders
from lambda_assistant.errors import *

# Wrapper expected for tests
def expected_builder(code = 200):
    return APIGatewayProxyResult(
                HTTPStatus=code, 
                Headers=CORSHeaders().buildHeaders(), 
                Body={})

    
class TestResponseBuilder:

    @pytest.mark.parametrize(
        'httpstatus, headers, body, expected',
        [
            (
                200,
                CORSHeaders(),
                {},
                expected_builder()
            ),
            (
                500,
                CORSHeaders(),
                {},
                expected_builder(code=500)
            )
        ],
    )
    def test_build_response(self, httpstatus, headers, body, expected: APIGatewayProxyResult):
        response = buildResponse(httpstatus, headers, body)
        response.Headers = headers.buildHeaders()
        
        assert isinstance(response, APIGatewayProxyResult)
        assert response == expected
        
        response = response.toDict()
        expected = expected.toDict()

        assert response['statusCode'] == expected['statusCode']
        assert response['headers'] == expected['headers']
        assert response['body'] == expected['body']
    
    
    @pytest.mark.parametrize(
        'operation, body, expected',
        [
            ("GET", {}, {'Operation': "GET", 'Response': json.dumps({})}),
            ("POST", {}, {'Operation': "POST", 'Response': json.dumps({})})
        ],
    )
    def test_builder_body(self, operation, body, expected):
        response = buildLambdaBody(operation, body)
        
        assert response['Operation'] == operation
        assert response['Response'] == json.dumps(body)
        assert response == expected