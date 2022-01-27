from dataclasses import dataclass
import os
import json

# Config file containing credentials enviroment

rds_host  = os.environ.get('rds_host')
db_username = os.environ.get('db_username')
db_password = os.environ.get('db_password')
db_name = os.environ.get('db_name')
    
class Config(object):
    
    @staticmethod 
    def GetDbConfig(path=None) -> dict:
        """ Return JSON configuration file """
        if rds_host is not None:
            return{
                'db_host': rds_host,
                'db_user': db_username,
                'db_pass': db_password,
                'db_name': db_name 
            }
        else:
            if path is not None:     
                with open(path) as f:
                    config = json.load(f)
                return config
            else:
                return {}
        