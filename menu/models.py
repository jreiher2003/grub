import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationships
from sqlalchemy import create_engine

Base = declarative_base()
#### class code #######
class Place(Base):
	__tablename__ = 'place' # names table
	id = Column(Integer, primary_key=True)
	name = Column(String(80), nullable=False)

########## insert at end of file ########
engine = create_engine('sqlite:///menu.db')
Base.metadata.create_all(engine)

