#models.py is for holding data having name and properties of the entry
from pydantic import BaseModel
class Product(BaseModel):
    id:int
    name:str
    description:str
    price:float
    quantity:int
