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

    def asdict(self) -> Dict[str, Any]:
        #Convert self into a dict.
        return {k: v for k, v in asdict(self).items() if v is not None}
        
    def asjson(self):
        #Convert self into a json response
        return json.dumps({
            "HTTPStatus": self.HTTPStatus,
            "Headers": self.Headers,
            "Body": json.dumps(self.Body)
        }, indent= 3)