import os

# Config file containing credentials enviroment
rds_host  = os.environ.get('rds_host')
db_username = os.environ.get('db_username')
db_password = os.environ.get('db_password')
db_name = os.environ.get('db_name')