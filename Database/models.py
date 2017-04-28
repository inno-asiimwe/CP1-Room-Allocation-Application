from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///andela.db', echo=True)
Base = declarative_base()

class Room(Base):
    """ """
    __tablename__ = "room"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    use = Column(String)

    def __init__ (self, name, use):
        self.name = name
        self.use = use

class Person(Base):
    """ """
    __tablename__ = 'person'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    role = Column(String)

    def __init__ (self, name, role):
        self.name = name
        self.role = role

class OfficeAllocation(Base):
    """"""
    __tablename__ = 'officeallocation'
    id = Column(Integer, primary_key = True)
    personid = Column(Integer)
    roomid = Column(Integer)

    def __init__ (self, personid, roomid):
        self.personid = personid
        self.roomid = roomid

class Livingallocation(Base):
    """"""
    __tablename__ = 'livingallocation'
    id = Column(Integer, primary_key = True)
    personid = Column(Integer)

    def __init__ (self, personid, roomid):
        self.personid = personid
        self.roomid = roomid

Base.metadata.create_all(engine)
