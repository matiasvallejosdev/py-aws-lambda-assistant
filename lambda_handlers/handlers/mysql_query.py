import asyncio

class mysql_query():
    def execute_select(self, conn, sql):
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

    def execute_delete(self, conn, sql, sql_recheckidentity):
        result = []

        # Execute SQL command
        with conn.cursor() as cur:
            cur.execute(sql)
            cur.execute(sql_recheckidentity)

        # Commit changes    
        conn.commit()        
        return result

    def execute_insert(self, conn, sql, get_id=False):
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