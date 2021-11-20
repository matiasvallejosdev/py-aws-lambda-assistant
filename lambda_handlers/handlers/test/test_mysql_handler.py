import pytest
import pymysql
import json

from lambda_handlers.handlers.mysql_handler import MySqlHandler
from lambda_handlers.handlers.lambda_handler import LambdaHandler

PATH_JSON = r'C:\Users\matia\Desktop\MATIAS A. VALLEJOS\Github\Github.Work\MiRegistro\Project.Backend\API\config\config.json'

class TestMySqlHandler:
    @pytest.fixture()
    def config(self):
        # Return JSON configuration file
        with open(PATH_JSON) as f:
            config = json.load(f)
            print(config)
        return config

    @pytest.fixture
    def conn(self, config):
        mySqlHandler = MySqlHandler(
            config["db_name"],
            config["rds_host"],
            config["db_username"],
            config["db_password"])
        conn = mySqlHandler.Connect()
        return conn
    
    @pytest.fixture
    def cur(self, conn):
        return conn.cursor()

    def test_mysql_connection_success(self, conn, cur):
        cur.execute("SELECT VERSION()")
        result = cur.fetchone()
        assert result
        assert isinstance(conn, pymysql.connections.Connection)
        assert isinstance(cur, pymysql.cursors.Cursor)

    """def test_invalid_body_validation(self, handler):
        with pytest.raises(FormatError, match='Unexpected type for JSON input'):
            handler({}, None)"""