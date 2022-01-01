import json

from lambda_handlers.errors import *
from lambda_handlers.types import *
from lambda_handlers.response.headers import Headers
from lambda_handlers.types import APIGatewayProxyResult


def buildResponse(operation, data, lambdaError=None):
    try:
        headers = Headers()
        if lambdaError is None:
            # If not have an lambda error
            return APIGatewayProxyResult(
                HTTPStatus=200, 
                Headers=headers.buildHeaders(), 
                Body=buildBody(operation=operation, response=data)
                )
        else:
            lambdaErrorJson = lambdaError.toJson() 
            # If have a lambda error
            return APIGatewayProxyResult(
                HTTPStatus=lambdaErrorJson['statusCode'], 
                Headers=headers.buildHeaders(), 
                Body=buildBody(operation=operation, response=lambdaErrorJson['error'])
                )
    except:
        # If have an internal server error reported
        lambdaErrorJson = LambdaError(error=InternalServerError()).toJson()
        return APIGatewayProxyResult(
                HTTPStatus=lambdaErrorJson['statusCode'], 
                Headers=headers.buildHeaders(), 
                Body=buildBody(operation="NULL /forgotten", response=lambdaErrorJson['error'])
                )    

def buildBody(operation, response):
        return {
        'Operation': operation,
        'Response': json.dumps(response, sort_keys=True, default=str)
        }

def buildResult(result):
        return {
        'Result': result
        }