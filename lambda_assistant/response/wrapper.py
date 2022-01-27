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
    
def buildBody(operation, response):
        return {
        'operationResource': operation,
        'response': json.dumps(response, default=str)
        }
        