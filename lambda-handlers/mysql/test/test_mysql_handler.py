import pytest
import pymysql
import json

from lambda_handlers.mysql.client_handler import *
from lambda_handlers.handlers.event_handler import *

PATH_JSON = r'C:\Users\matia\Desktop\Matias A. Vallejos\Github\Github.Work\MR-miregistro\miregistro-backend\src\backend\config\mysql_config.json'

class TestMySqlHandler:
    
    @pytest.mark.skip()
    @pytest.fixture
    def config(self):
        # Return JSON configuration file
        with open(PATH_JSON) as f:
            config = json.load(f)
            print(config)
        return config

    @pytest.mark.skip()
    @pytest.fixture
    def conn(self, config):
        mySqlHandler = MySqlHandler(
            config["db_name"],
            config["rds_host"],
            config["db_username"],
            config["db_password"])
        conn = mySqlHandler.Connect()
        return conn
    
    @pytest.mark.skip()
    @pytest.fixture
    def cur(self, conn):
        return conn.cursor()
    
    
    @pytest.mark.skip(reason="You need to add JSON Config for connection credentials")
    def test_mysql_connection_success(self, conn, cur):
        cur.execute("SELECT VERSION()")
        result = cur.fetchone()
        assert result
        assert isinstance(conn, pymysql.connections.Connection)
        assert isinstance(cur, pymysql.cursors.Cursor)

    """def test_invalid_body_validation(self, handler):
        with pytest.raises(FormatError, match='Unexpected type for JSON input'):
            handler({}, None)"""