from fastapi import FastAPI,Depends
from models import Product
from database import session,engine
import database_model
from sqlalchemy.orm import Session
app=FastAPI()

database_model.Base.metadata.create_all(bind=engine)


products = [
    Product(id=1,name="Laptop", description="15 inch gaming laptop", price=75000, quntity=10),
    Product(id=2,name="Mouse", description="Wireless optical mouse", price=800, quntity=50),
    Product(id=3,name="Keyboard", description="Mechanical keyboard", price=2500, quntity=30),
    Product(id=4,name="Monitor", description="24 inch LED monitor", price=12000, quntity=15),
    Product(id=5,name="Headphones", description="Noise cancelling headset", price=3500, quntity=25),
]



def init_db():
     db=session()
     count=db.query(database_model.Product).count
     if count==0:
        for product in products:
             db.add(database_model.Product(**product.model_dump()))
        db.commit()

init_db()

def get_db():
    db=session()
    try:
        yield db
    finally:
        db.close()

@app.get("/products")
def get_all_product(db:Session=Depends(get_db)):
    db_products=db.query(database_model.Product).all()
    return db_products

@app.get("/product/{id}")
def one_by_one(id:int,db:Session=Depends(get_db)):
    db_product=db.query(database_model.Product).filter(database_model.Product.id==id).first()
    if db_product:
        return db_product
    return "Product not found!"

@app.post("/product")
def create_pro(product: Product,db:Session=Depends(get_db)):
    product=db.add(database_model.Product(**product.model_dump()))
    db.commit()
    return product