import pymysql
from lambda_handlers.response.wrapper import buildResult

class Select():
    def Select(self, conn, sql):
        result = []

        # Execute SQL command
        with conn.cursor() as cur:
            cur.execute(sql)
            row_headers=[x[0] for x in cur.description] #this will extract row headers
            
            for row in cur:
                result.append(dict(zip(row_headers, row)))

        # Commit changes           
        conn.commit()
        #result.append(count)
        return buildResult(result)

class Delete():
    def Delete(self, conn, sql, sql_recheckidentity):
        result = []

        # Execute SQL command
        with conn.cursor() as cur:
            cur.execute(sql)
            cur.execute(sql_recheckidentity)

        # Commit changes    
        conn.commit()        
        return buildResult(result)

class Insert():
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
        return buildResult(result)
