import pymysql
from lambda_handlers.response.wrapper import *

class Select():
    def Select(self, conn: pymysql.connections.Connection, sql: str):
        result = []
        
        # Execute SQL command
        with conn.cursor() as cur:
            cur.execute(sql)
            row_headers=[x[0] for x in cur.description] #this will extract row headers
            
            for row in cur:
                result.append(dict(zip(row_headers, row)))

        # Commit changes           
        conn.commit()  
        return buildResult(result)

class Delete():
    def Delete(self, conn:pymysql.connections.Connection, sql: str, sql_recheckidentity: str):
        result = []

        # Execute SQL command
        with conn.cursor() as cur:
            cur.execute(sql)
            cur.execute(sql_recheckidentity)

        # Commit changes    
        conn.commit()        
        return buildResult(result)

class Insert():
    def Insert(self, conn: pymysql.connections.Connection, sql: str, get_id=False):
        result = []

        # Execute SQL command
        with conn.cursor() as cur:
            cur.execute(sql)
            if get_id:
                id = int(cur.lastrowid)
                result.append(id)

        # Commit changes    
        conn.commit()
        return buildResult(result)

class MySqlHandler(Select, Delete, Insert):
    def __init__(self, db_name, rds_host, db_username, db_password):
        self.rds_host = rds_host
        self.db_name = db_name
        self.db_username = db_username
        self.db_password = db_password

    def Connect(self):
        conn = pymysql.connect(host=self.rds_host, user=self.db_username, passwd=self.db_password, db=self.db_name, connect_timeout=5)
        return conn  
