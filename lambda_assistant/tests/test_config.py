import pytest

from lambda_assistant.config import *

class TestConfig:
    @pytest.fixture
    def path(self):
        path = r"C:\Users\matia\Desktop\Matias A. Vallejos\Github\Github.Work\miregistro-serverless-app\backend\src\config\mysql_config.json"
        return path
    
    def test_get_db_config_except(self):
        config = Config.GetDbConfig("except")
        assert config == {}
    
    def test_get_db_config_path(self, path):
        config = Config.GetDbConfig(path)
        assert config != {}
        
    def test_get_db_config_default(self, path):
        config = Config.GetDbConfig()
        assert config != {}