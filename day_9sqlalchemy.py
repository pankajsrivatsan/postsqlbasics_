from sqlalchemy import create_engine, String, Integer, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

engine= create_engine(
    "postgresql://postgres:postgres123@localhost/postgres"
)
#step:2 registry for all models
class Base(DeclarativeBase):
    pass



#model- one class one table
class Product(Base):
    __tablename__="products"

    id      : Mapped[int]   = mapped_column(Integer,primary_key=True)
    name    : Mapped[str]   = mapped_column(String(100))
    category: Mapped[str]   = mapped_column(String(50))
    price   : Mapped[float] = mapped_column(Float)
    stock   : Mapped[int]=mapped_column(Integer)

    def __repr__(self):
        return f"Product(name={self.name}, category={self.category}, price= {self.price}, stock= {self.stock})"
    

#drop and create fresh
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
print("table created!")


with Session(engine) as session:
    p1=Product(name='apple', category='fruit', price=1.50, stock=120)
    p2=Product(name='banana', category='fruit', price= 2.75, stock= 150)
    p3= Product(name='carrot', category= 'vegetable', price= 1.49, stock=100)
    p4=Product(name='mango', category= 'fruit', price= 4.00, stock=50)

    session.add_all([p1,p2,p3,p4])
    session.commit()
    print("inserted!")

    products=session.query(Product).filter(Product.id==1).first()
    print(products)

    fruit=session.query(Product).filter(Product.category=='fruit').all()
    for f in fruit:
        print(f)
    
    update=session.query(Product).filter(Product.name=='mango').first()
    update.price=3.00
    session.commit()
    print(update)

    banana=session.query(Product).filter(Product.name=='banana').first()
    session.delete(banana)
    session.commit()
    
    print("\nafter updates:")
    for p in session.query(Product).all():
        print(p)
    

