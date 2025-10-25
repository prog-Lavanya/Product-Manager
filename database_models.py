from sqlalchemy import Column,Integer,String,Float
from database import Base

class Product(Base):
    
    __tablename__="Products"

    id=Column(Integer,primary_key=True,index=True,autoincrement=True)
    name=Column(String)
    description=Column(String)
    price=Column(Float)
    quantity=Column(Integer)