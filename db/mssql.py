from sqlalchemy import create_engine
from db.connection import ConnectionString
from  utilities import constant
from db.dbbase import DBCore

class MsSqlDb(DBCore):
    '''This core class provide supporting function (CRUD Operations) for MS SQL Server.'''
    
    def __init__(self, connection_str):
        if connection_str is None:
            DBCore.__init__(self,ConnectionString(constant.DB_TYPE_MSSQL_SERVER).get_connection())
        else:
            DBCore.conn = connection_str