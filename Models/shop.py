from sqlalchemy.orm import *
from sqlalchemy import *

from Base import *


class Shop(Base):
    __tablename__ = "Shop"

    id = Column("id", Integer, primary_key=True, unique=True)
    OwnerId = mapped_column(ForeignKey("User.id"))

    SellerId = mapped_column(ForeignKey("Seller.id"))
    name = Column("name", String)
    address = Column("address", String)
