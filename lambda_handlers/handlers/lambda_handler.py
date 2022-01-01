from lambda_handlers.errors import *

class LambdaHandler():
    def __init__(self, event, context, lambdaError: LambdaError = None):
        self.event = event # event
        self.context = context # context
        self.lambdaError = lambdaError or None
    
    def performError(self, error):
        self.lambdaError = error
