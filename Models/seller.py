from sqlalchemy.orm import *
from sqlalchemy import *

from .Base import *

class Seller(Base):
    __tablename__ = "Seller"

    id = Column("id", Integer, primary_key=True, unique=True)
    Name = Column("Name", String)
    OwnerId = Column(ForeignKey("User.id"))