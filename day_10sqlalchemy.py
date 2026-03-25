from sqlalchemy import create_engine,String, Integer,Numeric, ForeignKey
from sqlalchemy.orm import DeclarativeBase ,Mapped  ,mapped_column, Session, relationship

engine=create_engine(
    "postgresql://postgres:postgres123@localhost/postgres"
)

class Base(DeclarativeBase):
    pass
#parent class
class Customer(Base):
    __tablename__="customers"

    id      : Mapped[int] = mapped_column(Integer, primary_key=True)
    name    : Mapped[str] = mapped_column(String(100))
    email   : Mapped[str] = mapped_column(String(150))
    city    : Mapped[str] = mapped_column(String(100))

    orders: Mapped[list["Order"]]= relationship("Order", back_populates="Customer")

    def __repr__(self):
        return f"Customer(name= {self.name}, city={self.city})"
    
class Order(Base):
    __tablename__="orders"

    id      : Mapped[int]   = mapped_column(Integer ,primary_key=True)
    customer_id: Mapped[int]    = mapped_column(Integer, ForeignKey("customers.id"))
    product : Mapped[str]   = mapped_column(String(100))
    amount   : Mapped[float] = mapped_column(Numeric)

    #relationship-- gives access to the customer who placed this orders
    customer: Mapped["Customer"] = relationship("Customer", back_populates="orders")

    def __repr__(self):
        return f"Order(product={self.product}, amount={self.amount})"
    

#drop and create
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

print("tables created!")

