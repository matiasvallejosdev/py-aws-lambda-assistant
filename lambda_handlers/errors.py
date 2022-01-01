# Class lambda error to manage common errors in execution time
from dataclasses import dataclass
import json
from http import HTTPStatus

class LambdaError():
    def __init__(self, error):
        self.statusCode = error._httpStatus
        self.type = error._type
        self.message = error._description

    def toJson(self):
        return {
            'statusCode': self.statusCode,
            'error': {
                'message': self.message,
                'type': self.type
            }
        }

    def toPrint(self):
        return "You get error with code {code} of type {type}".format(code=self.statusCode, type=self.type)
    
@dataclass
class InternalServerError():
    _httpStatus = HTTPStatus.INTERNAL_SERVER_ERROR.value
    _description = HTTPStatus.INTERNAL_SERVER_ERROR.description
    _type = 'internalServerError'
    
@dataclass
class BadRequestError():
    _httpStatus = HTTPStatus.BAD_REQUEST.value
    _description = HTTPStatus.BAD_REQUEST.description
    _type = 'badRequestError'
        
@dataclass
class NotFoundError():
    _httpStatus = HTTPStatus.NOT_FOUND.value
    _description = HTTPStatus.NOT_FOUND.description
    _type = 'notFoundError'

@dataclass
class PutDataFailedError():
    _httpStatus = HTTPStatus.NOT_ACCEPTABLE.value
    _description = HTTPStatus.NOT_ACCEPTABLE.description
    _type = 'putDataFailedError'

@dataclass
class PutDataFailedError():
    _httpStatus = HTTPStatus.NOT_ACCEPTABLE.value
    _description = HTTPStatus.NOT_ACCEPTABLE.description
    _type = 'getDataFailedError'

@dataclass
class DeleteDataFailedError():
    _httpStatus = HTTPStatus.BAD_REQUEST.value
    _description = HTTPStatus.BAD_REQUEST.description
    _type = 'deleteDataFailedError'

@dataclass
class ConflictConnectionError():
    _httpStatus = HTTPStatus.CONFLICT.value
    _description = HTTPStatus.CONFLICT.description
    _type = 'conflictConnectionError'