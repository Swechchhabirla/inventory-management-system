
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from app.database import SessionLocal, engine

from app.models import (
    Base,
    Product,
    Customer,
    Order,
    OrderItem
)
from app.schemas import (
    ProductCreate,
    CustomerCreate,
    OrderCreate
)

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "Inventory API Running"}

# CREATE PRODUCT
@app.post("/products")
def create_product(product: ProductCreate,
                   db: Session = Depends(get_db)):

    existing_product = db.query(Product).filter(
        Product.sku == product.sku
    ).first()

    if existing_product:
        return {
            "message": "SKU already exists"
        }

    if product.quantity < 0:
        return {
            "message": "Quantity cannot be negative"
        }

    new_product = Product(
        name=product.name,
        sku=product.sku,
        price=product.price,
        quantity=product.quantity
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product

# GET ALL PRODUCTS
@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return products
@app.get("/products/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):

    product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    if not product:
        return {"message": "Product not found"}

    return product
@app.delete("/products/{product_id}")
def delete_product(product_id: int,
                   db: Session = Depends(get_db)):

    product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    if not product:
        return {"message": "Product not found"}

    db.delete(product)
    db.commit()

    return {"message": "Product deleted"}
@app.put("/products/{product_id}")
def update_product(
    product_id: int,
    product: ProductCreate,
    db: Session = Depends(get_db)
):

    existing_product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    if not existing_product:
        return {"message": "Product not found"}

    existing_product.name = product.name
    existing_product.sku = product.sku
    existing_product.price = product.price
    existing_product.quantity = product.quantity

    db.commit()
    db.refresh(existing_product)

    return existing_product
@app.post("/customers")
def create_customer(
    customer: CustomerCreate,
    db: Session = Depends(get_db)
):

    existing_customer = db.query(Customer).filter(
        Customer.email == customer.email
    ).first()

    if existing_customer:
        return {
            "message": "Email already exists"
        }

    new_customer = Customer(
        full_name=customer.full_name,
        email=customer.email,
        phone=customer.phone
    )

    db.add(new_customer)

    db.commit()

    db.refresh(new_customer)

    return new_customer

@app.get("/customers")
def get_customers(db: Session = Depends(get_db)):

    customers = db.query(Customer).all()

    return customers
@app.get("/customers/{customer_id}")
def get_customer(
    customer_id: int,
    db: Session = Depends(get_db)
):

    customer = db.query(Customer).filter(
        Customer.id == customer_id
    ).first()

    if not customer:
        return {
            "message": "Customer not found"
        }

    return customer
@app.delete("/customers/{customer_id}")
def delete_customer(
    customer_id: int,
    db: Session = Depends(get_db)
):

    customer = db.query(Customer).filter(
        Customer.id == customer_id
    ).first()

    if not customer:
        return {
            "message": "Customer not found"
        }

    db.delete(customer)

    db.commit()

    return {
        "message": "Customer deleted"
    }

@app.post("/orders")
def create_order(
    order: OrderCreate,
    db: Session = Depends(get_db)
):

    customer = db.query(Customer).filter(
        Customer.id == order.customer_id
    ).first()

    if not customer:
        return {
            "message": "Customer not found"
        }

    new_order = Order(
        customer_id=order.customer_id,
        total_amount=0
    )

    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    total_amount = 0

    for item in order.items:

        product = db.query(Product).filter(
            Product.id == item.product_id
        ).first()

        if not product:
            return {
                "message": f"Product {item.product_id} not found"
            }

        if product.quantity < item.quantity:
            return {
                "message": f"Insufficient stock for {product.name}"
            }

        total_amount += (
            product.price * item.quantity
        )

        product.quantity -= item.quantity

        order_item = OrderItem(
            order_id=new_order.id,
            product_id=product.id,
            quantity=item.quantity,
            price=product.price
        )

        db.add(order_item)

    new_order.total_amount = total_amount

    db.commit()

    db.refresh(new_order)

    return new_order
@app.get("/orders")
def get_orders(db: Session = Depends(get_db)):

    orders = db.query(Order).all()

    return orders
@app.get("/orders/{order_id}")
def get_order(
    order_id: int,
    db: Session = Depends(get_db)
):

    order = db.query(Order).filter(
        Order.id == order_id
    ).first()

    if not order:
        return {
            "message": "Order not found"
        }

    return order

@app.delete("/orders/{order_id}")
def delete_order(
    order_id: int,
    db: Session = Depends(get_db)
):

    order = db.query(Order).filter(
        Order.id == order_id
    ).first()

    if not order:
        return {
            "message": "Order not found"
        }

    db.delete(order)

    db.commit()

    return {
        "message": "Order deleted"
    }

@app.get("/dashboard")
def dashboard(db: Session = Depends(get_db)):

    total_products = db.query(Product).count()

    total_customers = db.query(Customer).count()

    total_orders = db.query(Order).count()

    low_stock_products = db.query(Product).filter(
        Product.quantity < 10
    ).count()

    return {
        "total_products": total_products,
        "total_customers": total_customers,
        "total_orders": total_orders,
        "low_stock_products": low_stock_products
    }