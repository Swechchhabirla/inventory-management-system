from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    ForeignKey
)

from sqlalchemy.orm import (
    declarative_base,
    relationship
)

Base = declarative_base()


# --------------------
# PRODUCT TABLE
# --------------------

class Product(Base):

    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)

    sku = Column(String, unique=True)

    price = Column(Float)

    quantity = Column(Integer)


# --------------------
# CUSTOMER TABLE
# --------------------

class Customer(Base):

    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String)

    email = Column(String, unique=True)

    phone = Column(String)


# --------------------
# ORDER TABLE
# --------------------

class Order(Base):

    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)

    customer_id = Column(
        Integer,
        ForeignKey("customers.id")
    )

    total_amount = Column(Float)

    customer = relationship("Customer")


# --------------------
# ORDER ITEMS TABLE
# --------------------

class OrderItem(Base):

    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)

    order_id = Column(
        Integer,
        ForeignKey("orders.id")
    )

    product_id = Column(
        Integer,
        ForeignKey("products.id")
    )

    quantity = Column(Integer)

    price = Column(Float)

    product = relationship("Product")