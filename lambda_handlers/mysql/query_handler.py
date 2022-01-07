
from typing import Tuple
from lambda_handlers.response.wrapper import *

class Query():
    def __init__(self, base_query: str = None):
        self.sql = base_query or ""
        
    def GetQuery(self):
        return self.sql + ";"
        
    def PerformBase(self, base: str):
        self.sql = base
    
    def PerformWhere(self, where_instructions: Tuple):
        i = 0
        for query in where_instructions:
            if i == 0:
                self.sql = self.sql + " WHERE " + query
            else:
                self.sql = self.sql + " AND " + query
            i=i+1
        return self.sql
    
    def PerformGroupBy(self, groupBy: str):
        self.sql = self.sql + " GROUP BY {by}".format(by=groupBy)
        
    def PerformOrderBy(self, orderBy: str, order: str):
        self.sql = self.sql + " ORDER BY {by} {order}".format(by=orderBy, order=order)
        
    def PerformLimit(self, limit: int):
        self.sql = self.sql + " LIMIT {limit}".format(limit = limit)