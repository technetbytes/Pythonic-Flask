from db import mssql
from config.application import ApplicationConfiguration
from utilities import constant

class DbBridge:
    '''This is cache class that provide a bridge for different type of caches'''
    
    def __init__(self):
        self.configuration = ApplicationConfiguration(None)
        self.database_type = self.configuration.database
        self.environment = self.configuration.database
        self.debug = self.configuration.database
        self.db_session = None
        
    def get_application(self):
        return self.database_type

    def get_mode(self):
        return self.debug

    def get_environment(self):
        return self.environment  

    def load_db(self):
        if self.database_type == constant.DB_TYPE_MSSQL_SERVER:
            self.db_session = mssql.MsSqlDb(None)
    
    def get_data(self,query):
        if self.db_session is not None:
            return self.db_session.get_data(query)
    
    def get_data_forModel(self,model_type):
        if self.db_session is not None:
            return self.db_session.get_model_all(model_type)