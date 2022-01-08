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

def buildLambdaBody(operation, response):
        return {
        'Operation': operation,
        'Response': json.dumps(response, sort_keys=True, default=str)
        }

def buildResult(result):
        return {
        'Result': result
        }
        
