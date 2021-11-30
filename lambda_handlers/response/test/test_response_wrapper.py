from http import HTTPStatus
import pytest
from lambda_handlers.response.headers import Headers
from lambda_handlers.response.wrapper import *
from lambda_handlers.errors import LambdaError, internalError, notFound, putDataFailed, getDataFailed, deleteDataFailed, conflictConnection

# Wrapper for tests
def ok():
    """Return a response with OK status code."""
    return buildResponse(operation="GET", data={}, count=0, lambdaError=None)

def expected_lambda_error(err):
    """Return a response with LAMBDA ERROR status code."""
    lambdaError = err.toLambda()
    return buildResponse(operation="GET", data={}, count=0, lambdaError=lambdaError)

def internal_error(err):
    """Return a response with INTERNAL ERROR status code."""
    lambdaError = err.toLambda()
    return buildResponse(operation="NULL /forgotten", data={}, count=0, lambdaError=lambdaError)

class TestResponseBuilder:
    #'statusCode': 200, 
    #'headers': {'Headers': {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'}}, 
    #'body': '{"Operation": "GET /tramites", "Count": 1, 
    #"Response": [[2182, "AE343FG", "Modificacion Prenda", "No"]]}'}

    # TEST WITHOUT LAMBDA.
    @pytest.mark.parametrize(
        'operation, status_code, headers, body, expected',
        [
            ("GET",
            200, 
            Headers().buildHeaders(), 
            json.dumps(buildBody("GET", {}, 0)),
            ok())
        ],
    )
    def test_builder_without_lambda(self, operation, status_code, headers, body, expected):
        response = buildResponse(operation=operation, data={}, count=0, lambdaError=None)
        assert response == expected
        assert isinstance(response, APIGatewayProxyResult)

        response = json.loads(response.asjson())
        assert response['HTTPStatus'] == status_code
        assert response['Headers'] == headers
        assert response['Body'] == body
    
    
    # TEST WITH LAMBDA 
    @pytest.mark.parametrize(
        'operation, status_code, headers, body, lambda_error_response, expected',
        [
            ("GET",
            HTTPStatus.NOT_FOUND.value, 
            Headers().buildHeaders(), 
            buildBody("GET", {
                        'message': HTTPStatus.NOT_FOUND.description,
                        'type': 'notFound'
                    }, 
                    0),
            notFound().toLambda(),
            expected_lambda_error(notFound())
            ),
            
            ("GET",
            HTTPStatus.BAD_REQUEST.value, 
            Headers().buildHeaders(), 
            buildBody("GET", {
                        'message': HTTPStatus.BAD_REQUEST.description,
                        'type': 'deleteDataFailed'
                    }, 
                    0),
            deleteDataFailed().toLambda(),
            expected_lambda_error(deleteDataFailed())
            ),

            ("NULL /forgotten",
            HTTPStatus.INTERNAL_SERVER_ERROR.value, 
            Headers().buildHeaders(), 
            buildBody("NULL /forgotten", {
                        'message': HTTPStatus.INTERNAL_SERVER_ERROR.description,
                        'type': 'internalError'
                    }, 
                    0),
            internalError().toLambda(),
            internal_error(internalError())
            )
        ],
    ) 
    def test_builder_with_lambda(self, operation, status_code, headers, body, lambda_error_response, expected):
        response = buildResponse(operation=operation, data={}, count=0, lambdaError=lambda_error_response)
        assert response == expected
        assert isinstance(response, APIGatewayProxyResult)

        response = json.loads(response.asjson())
        assert response['HTTPStatus'] == status_code
        assert response['Headers'] == headers
        assert response['Body'] == json.dumps(body)
    

    @pytest.mark.parametrize(
        'operation, count, body, expected',
        [
            ("GET", 1, {}, buildBody(operation="GET", response={}, count=1)),
            ("POST", 0, {}, buildBody(operation="POST", response={}, count=0))
        ],
    )
    def test_builder_body(self, operation, count, body, expected):
        response = buildBody(operation, body, count)
        
        assert response['Response'] == json.dumps(body)
        assert response['Count'] == count
        assert response['Operation'] == operation
        assert response == expected

