from sqlalchemy.orm import *
from sqlalchemy import *

from .Base import *

class User(Base):

    __tablename__ = "User"

    id = Column("id", Integer, primary_key = True, unique = True)
    name = Column(Text, unique = True)
