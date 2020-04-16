from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, PickleType, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Project(Base):
    '''This is Project Keys sample Data model class.'''
    
    __tablename__ = "tProjectKeys2"
    __table_args__ = {"schema":"KnowHow.dbo"}

    id = Column(Integer, primary_key=True, nullable=False)
    webKey = Column(Text, nullable=False)
    mobileKey = Column(Text, nullable=True)
        
    def __repr__(self):
        return '<Project model {}>'.format(self.id)
