from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd

class DBCore:
    '''This core database class provide core operation like connection, session and others.'''
    
    def __init__(self, connection):
        self.engin = None
        self.connection = connection
        self.conn_str = None
        self.current_session = None
    
    def get_engine(self):
        self.engin = create_engine(self.connection)
        return self.engin
   
    def get_connection(self):
        if self.engin is not None:
            return self.engin.connect()
        else:
            return self.get_engine().connect()

    def begin_transaction(self):
        if self.engin is not None:
            self.get_connection().begin()
    
    def commit_transaction(self):
        if self.engin is not None:
            self.get_connection().commit()
            
    def get_data(self, query):
        return pd.read_sql_query(query, self.get_connection())
    
    def insert_data(self, insert_query):
        self.get_connection().execute(insert_query)
    
    def update_data(self, update_query):
        self.get_connection().execute(update_query)
    
    def delete_data(self, delete_query):
        self.get_connection().execute(delete_query)
    
    def get_session(self):
        engine = self.get_engine()
        Session = sessionmaker(bind=engine)
        self.current_session = Session()
        return self.current_session

    def add_in_session(self,model_type):
        if self.current_session is not None:
            self.current_session.add(model_type)
    
    def session_commit(self):
        if self.current_session is not None:
            self.current_session.commit()
    
    def session_close(self):
        if self.current_session is not None:
            self.current_session.close()
    
    def get_model_all(self,model_type):
        if self.current_session is not None:
            return self.current_session.query(model_type).all()
        else:
            self.get_session()
            return self.current_session.query(model_type).all()