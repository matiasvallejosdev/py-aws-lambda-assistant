from lambda_handlers.errors import *

class EventHandler():
    def __init__(self, event, context, lambdaError: LambdaError = None):
        self.event = event # event
        self.context = context # context
        self.lambdaError = lambdaError or None # error
    
    def hasError(self):
        if self.lambdaError is None:
            return False
        return True
        
    def performError(self, error):
        self.lambdaError = LambdaError(error)
