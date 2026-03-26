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

    orders: Mapped[list["Order"]]= relationship("Order", back_populates="customer")

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


with Session(engine) as session:
    #create customers
    c1= Customer(name= 'alice', email= 'alice@gmail', city= 'mumbai')
    c2= Customer(name= 'bobo', email= 'bobo@gmail.com', city= 'bangalore')
    c3= Customer(name= 'carol', email= 'carol@gmail.com', city= 'delhi')

    session.add_all([c1, c2, c3])
    session.commit()
    print("customers inserted!")

    o1= Order(customer_id= 1, product='laptop', amount= 75000)
    o2= Order(customer_id= 1, product= 'mouse', amount= 1500)
    o3= Order(customer_id=2, product= 'phone', amount= 45000)
    o4= Order(customer_id= 3, product= 'table', amount= 30000)
    o5= Order(customer_id= 3, product= 'keyboard', amount= 2000)

    session.add_all([o1,o2, o3, o4,o5])
    session.commit()
    print("orders inserted!")

    customers= session.query(Customer).all()
    print(f"\nall customers:")
    for c in customers:
        print(c)

    alice =session.query(Customer).filter(Customer.name=='alice').first()
    print("\nalice's orders")
    for order in alice.orders:
        print(order)

    order= session.query(Order).filter(Order.product== 'laptop').first()
    print(f"\nalaptop order placed by: {order.customer.name}")

    #get all orders above 10000
    big_orders= session.query(Order).filter(Order.amount >10000).all()
    print("\nbig orders:")
    for o in big_orders:
        print(o)

    #get total spent per customer
    from sqlalchemy import func
    totals= session.query(
        Customer.name ,
        func.sum(Order.amount).label('total_spent')

    ).join(Order).group_by(Customer.name).all()

    print("\ntotal spent per customer:")
    for name, total in totals:
        print(f"{name}: {total}")
