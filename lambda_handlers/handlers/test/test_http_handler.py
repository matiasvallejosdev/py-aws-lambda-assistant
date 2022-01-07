from typing import NewType
import pytest
import logging

from lambda_handlers.errors import *
from lambda_handlers.handlers.event_handler import *
from lambda_handlers.handlers.http_handler import *

context = NewType('LambdaContext', object)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# To test lambda function
@HTTPHandler(headers=CORSHeaders(origin='*', credentials=True))
def lambda_function(event, context):
    # Do something
    return buildBody(event['routeKey'], event['result'])
        
 
class TestHttpHandler:
    @pytest.fixture
    def handler(self):
        return HTTPHandler(headers=CORSHeaders('*', True))
    
    @pytest.mark.parametrize(
        'event, routeKey, bodyResponse',
        [
            ({ 'routeKey': '/GET Stock', 'result': "Hello world from lambda function!"}, "/GET Stock", "Hello world from lambda function!"),
            ({ 'routeKey': '/GET Colors', 'result': {'Red': 130, 'Blue': 200, 'Green': 255}}, "/GET Colors", {'Red': 130, 'Blue': 200, 'Green': 255}),
            ({ 'routeKey': '/GET Tramites', 'result': {'Patente': 'AA00XX'}}, "/GET Tramites", {'Patente': 'AA00XX'})
        ]
    )
    def test_lambda_function(self, handler, event, routeKey, bodyResponse):
        http_response = lambda_function(event, context)
   
        body = buildBody(routeKey, bodyResponse)
        result = buildResponse(200, handler.headers, body)
        expected = handler._create_response(result)
        
        assert http_response == expected
    
    def test_create_response_error(self, handler: HTTPHandler):
        lambdaErrorJson = LambdaError(BadRequestError()).toJson()
        body = buildBody(operation="NULL /forgotten", response=lambdaErrorJson['Error']) 
        result = buildResponse(500, handler.headers, body)
        response = handler._create_response(result)
        
        expected = APIGatewayProxyResult(500, body, handler._create_headers()).asjson()
        
        assert isinstance(response, str)
        assert response == expected
        
    def test_create_response_ok(self, handler: HTTPHandler):
        body = buildBody("GET", {})
        result = buildResponse(200, handler.headers, body)
        response = handler._create_response(result)
        
        expected = APIGatewayProxyResult(200, buildBody("GET", {}), handler._create_headers()).asjson()
        
        assert isinstance(response, str)
        assert response == expected
        
    
    def test_create_empty_headers(self):
        httpHanlder = HTTPHandler(headers={ 'MyOwnHeader': 30 })
        result = httpHanlder._create_headers()
        
        assert result == { 'MyOwnHeader': 30 }
        
    def test_create_without_argument_headers(self):
        httpHanlder = HTTPHandler()
        result = httpHanlder._create_headers()
        
        assert result == CORSHeaders().buildHeaders()
        
    def test_create_custom_headers(self):
        httpHanlder = HTTPHandler(headers=CORSHeaders('45646asd1', True))
        result = httpHanlder._create_headers()
        
        assert result == CORSHeaders('45646asd1', True).buildHeaders()