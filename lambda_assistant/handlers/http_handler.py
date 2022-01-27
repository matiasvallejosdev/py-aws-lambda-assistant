from typing import Any, Callable, Dict, Optional

import json
import logging

from lambda_assistant.errors import *
from lambda_assistant.handlers.event_handler import EventHandler
from lambda_assistant.response import headers
from lambda_assistant.response.headers import CORSHeaders
from lambda_assistant.response.wrapper import buildResponse, buildBody
from lambda_assistant.types import APIGatewayProxyResult

logger = logging.getLogger()
logger.setLevel(logging.INFO)

class HTTPHandler():
    def __init__(self, headers: Optional[CORSHeaders] = None):
        self.headers = headers or CORSHeaders(origin='*', credentials=False)
    
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            try:
                body = func(*args, **kwargs) # body -> dict
                print(body)
                
                if 'Error' in json.loads(body['response']):
                    # If has lambda error
                    lambdaErrorJson = json.loads(body['response'])
                    return self._create_response(buildResponse(lambdaErrorJson['Error']['statusCode'], self.headers, body))
                if body is not None:
                    # If has OK
                    return self._create_response(buildResponse(200, self.headers, body))          
            except Exception as e:
                # If have an internal server error
                lambdaErrorJson = LambdaError(InternalServerError, e).toDict()
                logger.error(e)
                body = buildBody(operation="NULL /forgotten", response=lambdaErrorJson)
                return self._create_response(buildResponse(lambdaErrorJson['Error']['statusCode'], self.headers, body)) 
        return wrapper
    
    def _create_response(self, result: APIGatewayProxyResult):
        result.Headers = self._create_headers()
        return result.toDict()
    
    def _create_headers(self):
        header = {}
        if type(self.headers) == dict:
            header = self.headers
        if type(self.headers) == CORSHeaders:
            header = self.headers.buildHeaders()
        return header