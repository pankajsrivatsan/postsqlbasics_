from dataclasses import dataclass
from typing import Optional

@dataclass
class Customer:
    customer_id: int
    name: str
    email: str
    city: str

@dataclass
class Product:
    product_id: int
    name: str
    category: str
    price: float
    stock: int

@dataclass
class Order:
    order_id: int
    customer_id: int  # ← FOREIGN KEY 1
    product_id: int   # ← FOREIGN KEY 2
    quantity: int
    order_date: str
    status: str

# DATA
customers = [
    Customer(101, "Alice Johnson", "alice@email.com", "New York"),
    Customer(102, "Bob Smith", "bob@email.com", "Los Angeles"),
    Customer(103, "Charlie Brown", "charlie@email.com", "Chicago"),
]

products = [
    Product(1, "Laptop Pro", "Electronics", 1200.00, 50),
    Product(2, "Wireless Mouse", "Electronics", 25.00, 200),
    Product(3, "Desk Chair", "Furniture", 300.00, 30),
    Product(4, "Monitor 27in", "Electronics", 400.00, 75),
]

orders = [
    Order(1, 101, 1, 2, "2025-01-15", "completed"),
    Order(2, 102, 2, 5, "2025-01-16", "completed"),
    Order(3, 101, 3, 1, "2025-01-17", "pending"),
    Order(4, 103, 1, 1, "2025-01-18", "completed"),
    Order(5, 102, 4, 2, "2025-01-19", "cancelled"),
]

def get_customer_by_id(customer_id:int)-> Optional[Customer]:
    for customer in customers:
        if customer.customer_id==customer_id:
            return customer
    return None

def get_product_by_id(product_id:int)->Optional[Product]:
    for product in products:
        if product.product_id==product_id:
            return product
    return None

def get_order_by_id(order_id:int)->Optional[Order]:
    for order in orders:
        if order.order_id==order_id:
            return order
    return None

def get_order_details(order_id:int):
    #get complete order information including customer and product details 
    #this joins 3 tables:
    #order, customer, products. etc;........... it's via foreign keys. 
    #step:1 get the order
    order=get_order_by_id(order_id)
    if not order:
        return None
    
    customer=get_customer_by_id(order.customer_id)
    #step:3 get product details
    product=get_product_by_id(order.product_id)

    #step:4 calculate derived fields (using data from all tables )
    unit_price=product.price if product else 0 
    subtotal=unit_price*order.quantity
    tax= subtotal*0.1
    total=subtotal+tax
    #step:5 return enriched data
    return {
        "order":order,
        "customer":customer,
        "product":product,
        "details":{
            "unit_price":unit_price,
            "quantity":order.quantity,
            "subtotal":subtotal,
            "tax":tax,
            "total":total

        }
    }




# TEST IT
result = get_order_details(1)
if result:
    print(f"=== ORDER #{result['order'].order_id} ===")
    print(f"\nCustomer:")
    print(f"  Name: {result['customer'].name}")
    print(f"  Email: {result['customer'].email}")
    print(f"  City: {result['customer'].city}")
    
    print(f"\nProduct:")
    print(f"  Name: {result['product'].name}")
    print(f"  Category: {result['product'].category}")
    print(f"  Unit Price: ${result['details']['unit_price']:,.2f}")
    
    print(f"\nOrder Details:")
    print(f"  Quantity: {result['details']['quantity']}")
    print(f"  Date: {result['order'].order_date}")
    print(f"  Status: {result['order'].status}")
    
    print(f"\nPricing:")
    print(f"  Subtotal: ${result['details']['subtotal']:,.2f}")
    print(f"  Tax (10%): ${result['details']['tax']:.2f}")
    print(f"  Total: ${result['details']['total']:,.2f}")