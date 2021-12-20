import pymysql

class MySqlHandler():
    def __init__(self, db_name, rds_host, db_username, db_password):
        self.rds_host = rds_host
        self.db_name = db_name
        self.db_username = db_username
        self.db_password = db_password

    def Connect(self):
        conn = pymysql.connect(host=self.rds_host, user=self.db_username, passwd=self.db_password, db=self.db_name, connect_timeout=5)
        return conn  
    
    def Select(self, conn, sql):
        result = []
        response = []
        count = 0

        # Execute SQL command
        with conn.cursor() as cur:
            cur.execute(sql)
            row_headers=[x[0] for x in cur.description] #this will extract row headers
            
            for row in cur:
                count += 1
                response.append(dict(zip(row_headers, row)))

        # Commit changes           
        conn.commit()
        result.append(count)
        result.append(response)
        return result

    def Delete(self, conn, sql, sql_recheckidentity):
        result = []

        # Execute SQL command
        with conn.cursor() as cur:
            cur.execute(sql)
            cur.execute(sql_recheckidentity)

        # Commit changes    
        conn.commit()        
        return result

    def Insert(self, conn, sql, get_id=False):
        result = []

        # Execute SQL command
        with conn.cursor() as cur:
            cur.execute(sql)
            if get_id:
                id = int(cur.lastrowid)
                result.append(id)

        # Commit changes    
        conn.commit()
        return result