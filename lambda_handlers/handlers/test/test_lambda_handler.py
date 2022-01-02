from lambda_handlers.errors import *
from lambda_handlers.handlers.lambda_handler import *

PATH_JSON = r'C:\Users\matia\Desktop\Matias A. Vallejos\Github\Github.Work\MR-miregistro\miregistro-backend\src\backend\config\mysql_config.json'

class TestMySqlHandler:
    def test_has_error(self):
        lambdaHandler = LambdaHandler(event=None, context=None)
        lambdaHandler.performError(PutDataFailedError())
        
        assert lambdaHandler.lambdaError is not None
        assert lambdaHandler.hasError() == True
        
    def test_has_not_error(self):
        lambdaHandler = LambdaHandler(event=None, context=None)
        
        assert lambdaHandler.lambdaError is None
        assert lambdaHandler.hasError() == False

    def test_perform_error(self):
        lambdaHandler = LambdaHandler(event=None, context=None)
        lambdaHandler.performError(BadRequestError())
        
        assert lambdaHandler.lambdaError is not None
        assert isinstance(lambdaHandler.lambdaError, LambdaError)
        assert lambdaHandler.lambdaError.toJson() == {
            'statusCode': 400,
            'error': {
                'message': "Bad request syntax or unsupported method",
                'type': 'badRequestError'
            }
        }