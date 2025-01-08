from sqlalchemy.orm import *
from sqlalchemy import *

class Base(DeclarativeBase):
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class product(Base):
    __tablename__ = "product"

    id = Column("id", Integer, primary_key= True, unique= True)
    shopId = mapped_column(ForeignKey("shop.id"))
    name = Column("name", String)
    price = Column("price", Integer)

class seller(Base):
    __tablename__ = "seller"

    id = Column("id", Integer, primary_key= True, unique= True)
    Name = Column("Name", String)

class shop(Base):
    __tablename__ = "shop"

    id = Column("id", Integer, primary_key= True, unique= True)
    SellerId = mapped_column(ForeignKey("seller.id"))
    name = Column("name", String)
    address = Column("address", String)



#path to database
SQLALCHEMY_DATABASE_URL = "sqlite:///./main.db"

#creating SQLAlchemy engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autoflush=False, bind=engine)
db = SessionLocal()