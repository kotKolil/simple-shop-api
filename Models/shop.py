from sqlalchemy.orm import *
from sqlalchemy import *

from .Base import *

class Shop(Base):
    __tablename__ = "Shop"

    id = Column("id", Integer, primary_key=True, unique=True)
    SellerId = mapped_column(ForeignKey("Seller.id"))
    name = Column("name", String)
    address = Column("address", String)