import pytest
from http import HTTPStatus

from lambda_handlers.response.wrapper import *
from lambda_handlers.response.headers import CORSHeaders
from lambda_handlers.errors import *

# Wrapper expected for tests
def expected_builder(code = 200):
    return APIGatewayProxyResult(
                HTTPStatus=code, 
                Headers=CORSHeaders(), 
                Body={})

    
class TestResponseBuilder:
    """
    #### 1. Test buildResponse()
    #### 2. Test buildBody()
    #### 3. Test buildResult()
    """
    # 1.
    @pytest.mark.parametrize(
        'httpstatus, headers, body, expected',
        [
            (
                200,
                CORSHeaders(origin='localhost', credentials=True),
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
        assert isinstance(response, APIGatewayProxyResult)
        
        response.Headers = headers.buildHeaders()
        expected.Headers = headers.buildHeaders()
        assert response == expected
        
        response = response.asdict()
        expected = expected.asdict()

        assert response['HTTPStatus'] == expected['HTTPStatus']
        assert response['Headers'] == expected['Headers']
        assert response['Body'] == expected['Body']
    
    # 2.
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
    
    # 3.
    @pytest.mark.parametrize(
        'result, expected',
        [
            ("RESULT_TEST", {'Result': "RESULT_TEST"})
        ],
    )
    def test_build_result(self, result, expected):
        response = buildResult(result)
        
        assert response['Result'] == expected['Result']
        assert response == expected