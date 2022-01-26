from lambda_handlers.errors import *
from lambda_handlers.handlers.event_handler import *

PATH_JSON = r'C:\Users\matia\Desktop\Matias A. Vallejos\Github\Github.Work\MR-miregistro\miregistro-backend\src\backend\config\mysql_config.json'

class TestEventHandler:
    def test_has_error(self):
        eventHandler = EventHandler(event=None, context=None)
        eventHandler.performError(PutDataFailedError())
        
        assert eventHandler.lambdaError is not None
        assert eventHandler.hasError() == True
        
    def test_has_not_error(self):
        eventHandler = EventHandler(event=None, context=None)
        
        assert eventHandler.lambdaError is None
        assert eventHandler.hasError() == False

    def test_perform_error(self):
        eventHandler = EventHandler(event=None, context=None)
        eventHandler.performError(BadRequestError())
        
        assert eventHandler.lambdaError is not None
        assert isinstance(eventHandler.lambdaError, LambdaError)
        assert eventHandler.lambdaError.toDict() == {
            'Error': {
                'statusCode': 400,
                'message': "Bad request syntax or unsupported method",
                'type': 'badRequestError'
            }
        }