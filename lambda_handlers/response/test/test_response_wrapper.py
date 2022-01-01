import pytest
from http import HTTPStatus

from lambda_handlers.response.headers import Headers
from lambda_handlers.response.wrapper import *
from lambda_handlers.errors import *

# Wrapper expected for tests
def expected_success():
    return APIGatewayProxyResult(
                HTTPStatus=200, 
                Headers=Headers().buildHeaders(), 
                Body=buildBody(operation="GET", response={})
                )

def expected_lambda_error(operation, error):
    lambdaErrorJson = error.toJson()
    return APIGatewayProxyResult(
                HTTPStatus=lambdaErrorJson['statusCode'], 
                Headers=Headers().buildHeaders(), 
                Body=buildBody(operation=operation, response=lambdaErrorJson['error'])
                )
    
class TestResponseBuilder:

    """
    Test wrapper response APIGatewayProxyResult with lambda errors and without errors
        - 'statusCode': 200, 
        - 'headers': {'Headers': {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'}}, 
        - 'body': '{"Operation": "GET /tramites", "Response": [[2182, "AE343FG", "Modificacion Prenda", "No"]]}'}
    """

    # Test lambda success
    @pytest.mark.parametrize(
        'operation, status_code, headers, body, expected',
        [
            ("GET",
            200, 
            Headers().buildHeaders(), 
            json.dumps(buildBody("GET", {})),
            expected_success())
        ],
    )
    def test_builder_without_lambda(self, operation, status_code, headers, body, expected):
        response = buildResponse(operation=operation, data={}, lambdaError=None)
        assert response == expected
        assert isinstance(response, APIGatewayProxyResult)

        response = json.loads(response.asjson())
        assert response['HTTPStatus'] == status_code
        assert response['Headers'] == headers
        assert response['Body'] == body
    

    # Test with lambda errors 
    @pytest.mark.parametrize(
        'operation, status_code, headers, body, lambda_error_response, expected',
        [
            ("GET",
            HTTPStatus.NOT_FOUND.value, 
            Headers().buildHeaders(), 
            {   'Operation': "GET", 
                'Response': json.dumps({
                        'message': HTTPStatus.NOT_FOUND.description,
                        'type': 'notFoundError'
                    })
            },
            LambdaError(NotFoundError()),
            expected_lambda_error("GET", LambdaError(NotFoundError()))
            ),  
            ("GET",
            HTTPStatus.BAD_REQUEST.value, 
            Headers().buildHeaders(), 
            {   'Operation': "GET", 
                'Response': json.dumps({
                        'message': HTTPStatus.BAD_REQUEST.description,
                        'type': 'deleteDataFailedError'
                    })
            },
            LambdaError(DeleteDataFailedError()),
            expected_lambda_error("GET", LambdaError(DeleteDataFailedError()))
            ),
            ("NULL /forgotten",
            HTTPStatus.INTERNAL_SERVER_ERROR.value, 
            Headers().buildHeaders(), 
            {   'Operation': "NULL /forgotten", 
                'Response': json.dumps({
                        'message': HTTPStatus.INTERNAL_SERVER_ERROR.description,
                        'type': 'internalServerError'
                    })
            },
            LambdaError(InternalServerError()),
            expected_lambda_error("NULL /forgotten", LambdaError(InternalServerError()))
            )
        ],
    ) 
    def test_builder_with_lambda(self, operation, status_code, headers, body, lambda_error_response, expected):
        response = buildResponse(operation=operation, data={}, lambdaError=lambda_error_response)
        assert response == expected
        assert isinstance(response, APIGatewayProxyResult)

        response = json.loads(response.asjson())
        assert response['HTTPStatus'] == status_code
        assert response['Headers'] == headers
        assert response['Body'] == json.dumps(body)
    
    # Test body wrapper
    @pytest.mark.parametrize(
        'operation, body, expected',
        [
            ("GET", {}, {'Operation': "GET", 'Response': json.dumps({})}),
            ("POST", {}, {'Operation': "POST", 'Response': json.dumps({})})
        ],
    )
    def test_builder_body(self, operation, body, expected):
        response = buildBody(operation, body)
        
        assert response['Operation'] == operation
        assert response['Response'] == json.dumps(body)
        assert response == expected
     
    # Test result wrapper
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