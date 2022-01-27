import pymysql
import logging

from lambda_assistant.handlers.event_handler import EventHandler
from lambda_assistant.errors import *

logger = logging.getLogger()
logger.setLevel(logging.INFO)

class Select():
    def Select(self, handler: EventHandler, conn: pymysql.connections.Connection, sql: str):
        try:  
            result = {}
            
            # Execute SQL command
            with conn.cursor() as cur:
                cur.execute(sql)
                row_headers=[x[0] for x in cur.description] #this will extract row headers
                for index, row in enumerate(cur):
                    result[index] = dict(zip(row_headers, row))
    
            # Commit changes           
            conn.commit()  
            return result
        except Exception as e:
            handler.performError(GetDataFailedError())
            logger.error(handler.lambdaError.toPrint())
            logger.error(e)
            return handler.lambdaError.toDict()

class Delete():
    def Delete(self, handler: EventHandler, conn:pymysql.connections.Connection, sql: str, sql_recheckidentity: str):
        try:
            result = {}
            
            # Execute SQL command
            with conn.cursor() as cur:
                cur.execute(sql)
                cur.execute(sql_recheckidentity)
    
            # Commit changes    
            conn.commit()        
            return result
        except Exception as e:
            handler.performError(DeleteDataFailedError())
            logger.error(handler.lambdaError.toPrint())
            logger.error(e)
            return handler.lambdaError.toDict()

class Insert():
    def Insert(self, handler: EventHandler, conn: pymysql.connections.Connection, sql: str, get_id=False):
        try:
            result = {}

            # Execute SQL command
            with conn.cursor() as cur:
                cur.execute(sql)
                if get_id:
                    id = int(cur.lastrowid)
                    result['id_inserted'] = id

            # Commit changes    
            conn.commit()
            return result
        except Exception as e:
            handler.performError(PutDataFailedError())
            logger.error(handler.lambdaError.toPrint())
            logger.error(e)
            return handler.lambdaError.toDict()

class MySqlHandler(Select, Delete, Insert):
    def __init__(self, db_name, rds_host, db_username, db_password):
        self.rds_host = rds_host
        self.db_name = db_name
        self.db_username = db_username
        self.db_password = db_password

    def Connect(self):
        conn = pymysql.connect(host=self.rds_host, user=self.db_username, passwd=self.db_password, db=self.db_name, connect_timeout=5)
        return conn  
