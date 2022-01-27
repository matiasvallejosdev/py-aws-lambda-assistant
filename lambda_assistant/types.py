from typing import Any, Dict, Union, Optional
from dataclasses import asdict, dataclass
import json

Headers = Dict[str, Union[str, bool, int]]

@dataclass
class APIGatewayProxyResult:
    # Key names are expected and given by AWS APIGateway specifications and must not be changed
    HTTPStatus: int
    Body: Union[str, Dict[str, Any]]
    Headers: Optional[Headers] = None

    def toDict(self):
        #Convert self into a json response
        return {
            'statusCode': self.HTTPStatus,
            'headers': self.Headers,
            'body': json.dumps(self.Body)
        }