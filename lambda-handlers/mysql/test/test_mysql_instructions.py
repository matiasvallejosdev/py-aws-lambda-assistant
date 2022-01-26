import pytest
import pymysql
import json

from lambda_handlers.mysql.client_handler import *
from lambda_handlers.handlers.event_handler import *
from lambda_handlers.mysql.query_handler import Query

PATH_JSON = r'C:\Users\matia\Desktop\Matias A. Vallejos\Github\Github.Work\MR-miregistro\miregistro-backend\src\backend\config\mysql_config.json'

class TestMySqlInstructions:
    @pytest.fixture
    def base(self):
        # Return JSON configuration file
        return "SELECT * FROM Tramites"
    
    @pytest.mark.parametrize(
        'expected',
        [
            "SELECT * FROM Tramites;"
        ]
    )
    def test_instruction_get_query(self, base, expected):
        queryHandler = Query(base_query=base)  
        assert queryHandler.GetQuery() == expected 
        
    @pytest.mark.parametrize(
        'expected',
        [
            "SELECT * FROM Formularios;"
        ]
    )
    def test_instruction_perform_base(self, expected):
        queryHandler = Query()
        queryHandler.PerformBase("SELECT * FROM Formularios")
        
        assert queryHandler.GetQuery() == expected 
        
    @pytest.mark.parametrize(
        'where_instructions, expected',
        [
            (["F.Id = 1"], "SELECT * FROM Tramites WHERE F.Id = 1;"),
            (["F.Id = 1", "F.Dominio = AA000XX"], "SELECT * FROM Tramites WHERE F.Id = 1 AND F.Dominio = AA000XX;"),
            (["F.Id = 1", "F.Dominio = AA000XX", "F.Categoria = 2"], "SELECT * FROM Tramites WHERE F.Id = 1 AND F.Dominio = AA000XX AND F.Categoria = 2;")
        ]
    )
    def test_instruction_perform_base(self, base, where_instructions, expected):
        queryHandler = Query(base_query=base)
        queryHandler.PerformWhere(where_instructions)
        
        assert queryHandler.GetQuery() == expected 
        
    @pytest.mark.parametrize(
        'limit, expected',
        [
            (10, "SELECT * FROM Tramites LIMIT 10;"),
            (50, "SELECT * FROM Tramites LIMIT 50;")
        ]
    )
    def test_instruction_perform_limit(self, base, limit, expected):
        queryHandler = Query(base_query=base)
        queryHandler.PerformLimit(limit)
        
        assert queryHandler.GetQuery() == expected 
        
    @pytest.mark.parametrize(
        'orderBy, order, expected',
        [
            ("T.Id", "ASC", "SELECT * FROM Tramites ORDER BY T.Id ASC;")
        ]
    )
    def test_instruction_perform_order_by(self, base, orderBy, order, expected):
        queryHandler = Query(base_query=base)
        queryHandler.PerformOrderBy(orderBy, order)
        
        assert queryHandler.GetQuery() == expected 
        
    @pytest.mark.parametrize(
        'groupBy, expected',
        [
            ("T.Id", "SELECT * FROM Tramites GROUP BY T.Id;")
        ]
    )
    def test_instruction_perform_group_by(self, base, groupBy, expected):
        queryHandler = Query(base_query=base)
        queryHandler.PerformGroupBy(groupBy)
        
        assert queryHandler.GetQuery() == expected 