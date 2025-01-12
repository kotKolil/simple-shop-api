from sqlalchemy.orm import *
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy import *

from .Base import *

class Product(Base):
    __tablename__ = "Product"

    id = Column("id", Integer, primary_key=True, unique=True)
    shopId = mapped_column(ForeignKey("Shop.id"))
    name = Column("name", String)
    price = Column("price", Integer)

