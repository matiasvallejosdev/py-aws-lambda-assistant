import json

from lambda_handlers.handlers.lambda_handler import LambdaHandler
from lambda_handlers.errors import LambdaError, InternalServerError
from lambda_handlers.response.headers import Headers
from lambda_handlers.types import APIGatewayProxyResult


def buildResponse(operation, data: dict, lambdaHandler : LambdaHandler):
    try:
        if lambdaHandler.hasError():
            lambdaErrorJson = lambdaHandler.lambdaError.toJson() 
            # If have a generic lambda error
            return APIGatewayProxyResult(
                HTTPStatus=lambdaErrorJson['statusCode'], 
                Headers=Headers().buildHeaders(), 
                Body=buildBody(operation=operation, response=lambdaErrorJson['error'])
            )
        else:
            # If not have an lambda error
            return APIGatewayProxyResult(
                HTTPStatus=200, 
                Headers=Headers().buildHeaders(), 
                Body=buildBody(operation=operation, response=data)
            )
    except:
        lambdaErrorJson = LambdaError(InternalServerError()).toJson()
        # If have an internal server error
        return APIGatewayProxyResult(
                HTTPStatus=lambdaErrorJson['statusCode'], 
                Headers=Headers().buildHeaders(), 
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
        