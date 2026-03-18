from dataclasses import dataclass
from typing import Optional

@dataclass
class Customer:
    customer_id: int
    name: str
    email: str
    city: str

@dataclass
class Order:
    order_id: int
    customer_id: int  # ← FOREIGN KEY (connects to Customer)
    product: str
    amount: float
    status: str

# DATA
customers = [
    Customer(101, "Alice Johnson", "alice@email.com", "New York"),
    Customer(102, "Bob Smith", "bob@email.com", "Los Angeles"),
    Customer(103, "Charlie Brown", "charlie@email.com", "Chicago"),
]

orders = [
    Order(1, 101, "Laptop", 1200.00, "completed"),
    Order(2, 101, "Mouse", 25.00, "completed"),
    Order(3, 102, "Keyboard", 80.00, "completed"),
    Order(4, 101, "Monitor", 300.00, "pending"),
    Order(5, 103, "Laptop", 1200.00, "completed"),
    Order(6, 102, "Mouse", 25.00, "cancelled"),
]
def get_customer_by_id(customer_id:int)-> Optional[Customer]:
    for customer in customers:
        if customer.customer_id==customer_id:
            return customer
    return None
    
def get_customer_with_orders(customer_id:int):
    customer=get_customer_by_id(customer_id)
    if not customer:
        return None
    
    customer_orders=[o for o in orders if o.customer_id==customer_id]
    total_orders=len(customer_orders)

    completed_orders=[o for o in customer_orders if o.status =="completed" ]
    total_spent=sum(o.amount for o in completed_orders)

    return {
        "customer":customer,
        "orders":customer_orders,
        "stats":{
            "total_orders":total_orders,
            "completed_orders":len(completed_orders),
            "total_spent":total_spent,
            "average_order":total_spent/len(completed_orders) if completed_orders else 0 
        }
    }

result = get_customer_with_orders(102)
if result:
    print(f"Customer: {result['customer'].name}")
    print(f"Email: {result['customer'].email}")
    print(f"\nOrder History:")
    for order in result['orders']:
        print(f"  - {order.product}: ${order.amount:.2f} ({order.status})")
    print(f"\nStats:")
    print(f"  Total Orders: {result['stats']['total_orders']}")
    print(f"  Completed: {result['stats']['completed_orders']}")
    print(f"  Total Spent: ${result['stats']['total_spent']:.2f}")
    print(f"  Avg Order: ${result['stats']['average_order']:.2f}")