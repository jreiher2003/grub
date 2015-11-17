import sys
# from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()
#### class code #######
class Place(Base):
	__tablename__ = 'place' # names table
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), nullable=False)

########## insert at end of file ########
# engine = db.create_engine('sqlite:///menu.db')
# Base.metadata.db.create_all(engine)
