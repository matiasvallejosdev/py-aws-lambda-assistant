# Class lambda error to manage common errors in execution time
import json
from http import HTTPStatus

class LambdaError():
    def __init__(self, statuscode='', message='', type=''):
        self.statusCode = statuscode
        self.message = message
        self.type = type

    def toLambda(self):
        return {
            'statusCode': self.statusCode,
            'error': {
                'message': self.message,
                'type': self.type
            }
        }

   
def internalError():
    error = LambdaError(HTTPStatus.INTERNAL_SERVER_ERROR.value, HTTPStatus.INTERNAL_SERVER_ERROR.description, 'internalError')
    error.message = HTTPStatus.INTERNAL_SERVER_ERROR.description
    return error

def sqlError():
    error = LambdaError(HTTPStatus.BAD_REQUEST.value, HTTPStatus.BAD_REQUEST.description, 'sqlQueryError')
    error.message = HTTPStatus.BAD_REQUEST.description
    return error

def notFound():
    error = LambdaError(HTTPStatus.NOT_FOUND.value, HTTPStatus.NOT_FOUND.description, 'notFound')
    error.message = HTTPStatus.NOT_FOUND.description
    return error

def putDataFailed():
    error = LambdaError(HTTPStatus.NOT_ACCEPTABLE.value, HTTPStatus.NOT_ACCEPTABLE.description, 'putDataFailed')
    error.message = HTTPStatus.NOT_ACCEPTABLE.description
    return error

def getDataFailed():
    error = LambdaError(HTTPStatus.NOT_ACCEPTABLE.value, HTTPStatus.NOT_ACCEPTABLE.description, 'getDataFailed')
    error.message = HTTPStatus.NOT_ACCEPTABLE.description
    return error

def deleteDataFailed():
    error = LambdaError(HTTPStatus.BAD_REQUEST.value, HTTPStatus.BAD_REQUEST.description, 'deleteDataFailed')
    error.message = HTTPStatus.BAD_REQUEST.description
    return error

def conflictConnection():
    error = LambdaError(HTTPStatus.CONFLICT.value, HTTPStatus.CONFLICT.description, 'conflictConnection')
    error.message = HTTPStatus.CONFLICT.description
    return error
