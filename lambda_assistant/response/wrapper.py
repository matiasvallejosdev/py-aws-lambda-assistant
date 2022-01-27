import json

from lambda_assistant.handlers.event_handler import EventHandler
from lambda_assistant.errors import LambdaError, InternalServerError
from lambda_assistant.response.headers import CORSHeaders
from lambda_assistant.types import APIGatewayProxyResult

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
        