from typing import Any, Callable, Dict, Optional

from lambda_handlers.errors import *
from lambda_handlers.handlers.event_handler import EventHandler
from lambda_handlers.response import headers
from lambda_handlers.response.headers import CORSHeaders
from lambda_handlers.response.wrapper import buildResponse, buildBody
from lambda_handlers.types import APIGatewayProxyResult

class HTTPHandler():
    def __init__(self, headers: Optional[CORSHeaders] = None):
        self.headers = headers or CORSHeaders(origin='*', credentials=False)
    
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            try:
                body = func(*args, **kwargs) # body -> dict
                if 'Error' in body['Response']:
                    # If has lambda error
                    lambdaErrorJson = body['Response']['Error']
                    return self._create_response(buildResponse(lambdaErrorJson['statusCode'], self.headers, body))
                if body is not None:
                    # If has OK
                    return self._create_response(buildResponse(200, self.headers, body))          
            except:
                # If have an internal server error
                lambdaErrorJson = LambdaError(InternalServerError()).toJson()
                body = buildBody(operation="NULL /forgotten", response=lambdaErrorJson['Error'])
                return self._create_response(buildResponse(lambdaErrorJson['statusCode'], self.headers, body)) 
        return wrapper
    
    def _create_response(self, result: APIGatewayProxyResult):
        result.Headers = self._create_headers()
        return result.asjson()
    
    def _create_headers(self):
        header = {}
        if type(self.headers) == dict:
            header = self.headers
        if type(self.headers) == CORSHeaders:
            header = self.headers.buildHeaders()
        return header