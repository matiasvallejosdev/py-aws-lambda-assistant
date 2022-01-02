import pymysql
from lambda_handlers.handlers.mysql.mysql_operations import *

class MySqlHandler(Select, Delete, Insert):
    def __init__(self, db_name, rds_host, db_username, db_password):
        self.rds_host = rds_host
        self.db_name = db_name
        self.db_username = db_username
        self.db_password = db_password

    def Connect(self):
        conn = pymysql.connect(host=self.rds_host, user=self.db_username, passwd=self.db_password, db=self.db_name, connect_timeout=5)
        return conn  