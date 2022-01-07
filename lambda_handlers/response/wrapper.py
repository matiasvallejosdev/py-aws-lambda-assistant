import json

from lambda_handlers.handlers.event_handler import EventHandler
from lambda_handlers.errors import LambdaError, InternalServerError
from lambda_handlers.response.headers import CORSHeaders
from lambda_handlers.types import APIGatewayProxyResult


def buildResponse(statusCode, headers: dict, body: dict):
    return APIGatewayProxyResult(
            HTTPStatus=statusCode, 
            Headers=headers,
            Body= body
        )    
"""
def buildResponse(operation, data: dict, eventHandler : EventHandler):
    headersHandler = headersHandler or Headers(origin='*', credentials=False)
    try:
        if eventHandler.hasError():
            lambdaErrorJson = eventHandler.lambdaError.toJson() 
            # If have a generic lambda error
            return APIGatewayProxyResult(
                HTTPStatus=lambdaErrorJson['statusCode'], 
                Headers=headersHandler.buildHeaders(), 
                Body=buildBody(operation=operation, response=lambdaErrorJson['error'])
            )
        else:
            # If not have an lambda error
            return APIGatewayProxyResult(
                HTTPStatus=200, 
                Headers=headersHandler.buildHeaders(), 
                Body=buildBody(operation=operation, response=data)
            )
    except:
        lambdaErrorJson = LambdaError(InternalServerError()).toJson()
        # If have an internal server error
        return APIGatewayProxyResult(
                HTTPStatus=lambdaErrorJson['statusCode'], 
                Headers=headersHandler.buildHeaders(), 
                Body=buildBody(operation="NULL /forgotten", response=lambdaErrorJson['error'])
                )    
"""
def buildLambdaBody(operation, response):
        return {
        'Operation': operation,
        'Response': json.dumps(response, sort_keys=True, default=str)
        }

def buildResult(result):
        return {
        'Result': result
        }
        