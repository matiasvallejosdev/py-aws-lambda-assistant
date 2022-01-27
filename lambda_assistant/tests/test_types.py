import pytest

from lambda_assistant.response.headers import CORSHeaders
from lambda_assistant.types import *

class TestTypes:
    @pytest.fixture
    def default(self):
        default = APIGatewayProxyResult(200, {}, CORSHeaders())
        return default
    
    def test_get_db_config_except(self, default: APIGatewayProxyResult):
        d = default.toDict()
        
        assert 'statusCode' in d
        assert 'headers' in d
        assert 'body' in d
        
        