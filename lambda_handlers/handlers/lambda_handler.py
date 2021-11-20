
class LambdaHandler():
    def __init__(self, event, context, lambdaError = None):
        self.event = event # event
        self.context = context # context
        self.lambdaError = lambdaError # lambda error