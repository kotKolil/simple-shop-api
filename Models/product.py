from sqlalchemy.orm import *
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy import *

from .Base import *

class Product(Base):
    __tablename__ = "Product"

    shopId = mapped_column(ForeignKey("Shop.id"))
    OwnerId = mapped_column(ForeignKey("User.id"))

    id = Column("id", Integer, primary_key=True, unique=True)
    name = Column("name", String)
    price = Column("price", Integer)
