from sqlalchemy import create_engine, String , Integer, Numeric, ForeignKey, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship

engine= create_engine(
    "postgresql://postgres:postgres123@localhost/postgres"
)

class Base(DeclarativeBase):
    pass
class Customer(Base):
    __tablename__= "customers"
    id      : Mapped[int]= mapped_column(Integer, primary_key=True)
    name    : Mapped[str]= mapped_column(String(100))
    city    : Mapped[str]= mapped_column(String(100))
    orders  : Mapped[list['Order']]= relationship("Order", back_populates="customer")

    def __repr__(self):
        return f"Customer(name= {self.name}, city={self.city})"
    
class Order(Base):
    __tablename__ = "orders"
    id      : Mapped[int]   = mapped_column(Integer, primary_key=True)
    customer_id : Mapped[int] = mapped_column(Integer, ForeignKey("customers.id"))
    product     : Mapped[str]   = mapped_column(String(100))
    amount      : Mapped[float]  = mapped_column(Numeric)
    customer    :Mapped["Customer"] = relationship("Customer", back_populates="orders")

    def __repr__(self):
        return f"Order(product={self.product}, amount= {self.amount})"

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

with Session(engine) as session:
    #insert data
    c1= Customer(name= 'alice',city= 'mumbai')
    c2= Customer(name= 'bob', city= 'delhi')
    c3= Customer(name= 'carol', city= 'bangalore')
    session.add_all([c1, c2, c3])
    session.commit()

    o1=Order(customer_id=1, product='laptop', amount= 75000)
    o2=Order(customer_id=1 , product='mouse', amount= 1500)
    o3=Order(customer_id=2, product='phone', amount= 45000)
    o4=Order(customer_id=3, product='tablet', amount= 30000)
    o5=Order(customer_id=3, product='keyboard', amount= 2000)
    session.add_all([o1, o2, o3, o4, o5])
    session.commit()
    print("data ready!\n")


    #1. order by
    print("orders by amount high to low. ")
    orders=session.query(Order).order_by(Order.amount.desc()).all()
    for o in orders:
        print(o)

    #2. limit
    print("\ntop 2 most expensive orders:")
    top2= session.query(Order).order_by(Order.amount.desc()).limit(2).all()
    for o in top2:
        print(o)

    #3.count
    total= session.query(func.count(Order.id)).scalar()
    print(f"\ntotal orders: {total}")

    #4. sum
    total_revenue= session.query(func.sum(Order.amount)).scalar()
    print(f"total revenue: {total_revenue}")

    #5. avg
    avg_order= session.query(func.avg(Order.amount)).scalar()
    print(f"average orders: {round(float(avg_order), 2)}")

    #6.group by
    print("\ntotal spent per customer:")
    results= session.query(
        Customer.name,
        func.sum(Order.amount).label('total')

    ).join(Order).group_by(Customer.name).all()
    for name, total in results:
        print(f"{name}: {total}")

    #7. filter multiple conditions
    print("\nalice's orders above 1000:")
    results= session.query(Order).join(Customer).filter(
        Customer.name == 'alice',
        Order.amount >1000
    ).all()
    for o in results:
        print(o)

