from lambda_handlers.errors import LambdaError, internalError, notFound
from lambda_handlers.types import *
from lambda_handlers.response.headers import Headers
from lambda_handlers.types import APIGatewayProxyResult

import json

def buildResponse(operation, data, count, lambdaError=None):
    try:
        headers = Headers()
        if lambdaError is None:
            # If not have an lambda error
            return APIGatewayProxyResult(
                HTTPStatus=200, 
                Headers=headers.buildHeaders(), 
                Body=buildBody(operation=operation, response=data, count=count)
                )
        else:
            # If have a lambda error
            return APIGatewayProxyResult(
                HTTPStatus=lambdaError['statusCode'], 
                Headers=headers.buildHeaders(), 
                Body=buildBody(operation=operation, response=lambdaError['error'], count=count)
                )
    except:
        # If have an internal server error reported
        lambdaError = internalError().toLambda()
        return APIGatewayProxyResult(
                HTTPStatus=lambdaError['statusCode'], 
                Headers=headers.buildHeaders(), 
                Body=buildBody(operation="NULL /forgotten", response=lambdaError['error'], count=0)
                )    

def buildBody(operation, response, count):
        return {
        'Operation': operation,
        'Count': count,
        'Response': json.dumps(response, sort_keys=True, default=str)
        }