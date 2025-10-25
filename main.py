from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Product
from database import SessionLocal,engine
from database_models import Base,Product as ProductDB
app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],   
    allow_headers=["*"], 
)
Base.metadata.create_all(bind=engine)

@app.get("/")                       # @->decorator"  "\"-> root path 
def root():                         #function
    return {"message": "Welcome to mu api "}

products=[
    Product(id=1,name="Phone",description="Samsung",price=99,quantity=10),
    Product(id=2,name="Laptop",description="Dell",price=999,quantity=100), 
    Product(id=6,name="Laptop",description="Dell",price=999,quantity=100),
]

def init_db():
    db=SessionLocal()
    try:
        for product in products:
            data = product.model_dump()
            data.pop("id",None)
            existing = db.query(ProductDB).filter_by(id=product.id).first()
            if not existing:
                db.add(ProductDB(**data))
        db.commit()
        print("Database initialized.")
    except Exception as e:
        db.rollback()
        print("Error during init_db:", e)
    finally:
        db.close()

@app.get("/products") 
def get_all_products():
    db=SessionLocal()
    products=db.query(ProductDB).all()
    db.close()
    return products

@app.get("/products/{id}")
def get_product_by_id(id:int):
    db=SessionLocal()
    product=db.query(ProductDB).filter(ProductDB.id==id).first()
    db.close()
    if product:
        return product
    return "product not found"

@app.post("/products")
def add_product(product:Product):
    db=SessionLocal()
    new_product=ProductDB(**product.model_dump())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    db.close()
    return new_product

@app.put("/products/{id}")
def update_product(id: int,update_data:Product):
    db = SessionLocal()
    try:
        product = db.query(ProductDB).filter(ProductDB.id == id).first()
        if not product:
            return {"error!!":"Product not found"}
        for key, value in update_data.model_dump(exclude_unset=True).items():
            if key != "id":
                setattr(product, key, value)

        db.commit()
        db.refresh(product)
        return {"message": "Product updated successfully", "product": product}
    except Exception as e:
        db.rollback()
        return {"error": str(e)}
    finally:
        db.close()

@app.delete("/products/{id}")
def delete_product(id:int ):
    db = SessionLocal()
    try:
        product_db = db.query(ProductDB).filter(ProductDB.id == id).first()
        if not product_db:
            return {"error": "Product not found"}

        db.delete(product_db)
        db.commit()
        return {"message": f"Product deleted successfully"}
    except Exception as e:
        db.rollback()
        return {"error": str(e)}
    finally:
        db.close()

