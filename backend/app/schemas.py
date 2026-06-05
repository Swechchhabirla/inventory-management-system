from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    sku: str
    price: float
    quantity: int

class CustomerCreate(BaseModel):

    full_name: str
    email: str
    phone: str

class OrderItemCreate(BaseModel):

    product_id: int

    quantity: int
class OrderCreate(BaseModel):

    customer_id: int

    items: list[OrderItemCreate]
