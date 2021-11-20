
class mysql_query():
    def execute_select(self, conn, sql):
        self.result = []
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
        self.result.append(count)
        self.result.append(response)
        return self.result