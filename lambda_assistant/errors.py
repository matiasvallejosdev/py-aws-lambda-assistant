# Class lambda error to manage common errors in execution time
from dataclasses import dataclass
from http import HTTPStatus

class LambdaError():
    def __init__(self, error, message = None):
        self.statusCode = error._httpStatus
        self.type = error._type
        self.message = message or ""
        self.description = error._description

    def toDict(self):
        return {
            'Error': {
                'statusCode': self.statusCode,
                'message': self.message,
                'description': self.description,
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
class PreconditionRequiredError():
    _httpStatus = HTTPStatus.PRECONDITION_REQUIRED.value
    _description = HTTPStatus.PRECONDITION_REQUIRED.description
    _type = 'preconditionRequiredError'
    
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
class GetDataFailedError():
    _httpStatus = HTTPStatus.CONFLICT.value
    _description = HTTPStatus.CONFLICT.description
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