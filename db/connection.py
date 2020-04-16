from  utilities import constant
from config.database import DatabaseConfiguration

class ConnectionString:
    '''Provider database connection string'''
    
    def __init__(self,db_type):
        self.type = db_type
    
    def get_connection(self):
        db_config = DatabaseConfiguration(None)
        SERVER_ADDRESS = db_config.host
        DATABASE_NAME = db_config.db_name
        DRIVER_NAME = db_config.driver
        USER_NAME = db_config.username
        PASSWORD = db_config.password
        if self.type == constant.DB_TYPE_MSSQL_SERVER:
            return f'mssql+pyodbc://{USER_NAME}:{PASSWORD}@{SERVER_ADDRESS}/{DATABASE_NAME}?driver={DRIVER_NAME}'
        elif self.type == constant.DB_TYPE_MYSQL_SERVER:
            return ""
        elif self.type == constant.DB_TYPE_ORACLE:
            return ""
        elif self.type == constant.DB_TYPE_POSTGRESQL:
            return ""