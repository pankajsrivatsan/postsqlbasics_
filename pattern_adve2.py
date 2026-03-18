from dataclasses import dataclass
from typing import Optional
from collections import defaultdict

@dataclass
class Customer:
    customer_id: int
    name: str
    email: str
    city: str
    member_since: str

@dataclass
class Order:
    order_id: int
    customer_id: int  # ← FOREIGN KEY
    product: str
    amount: float
    status: str  # "completed", "pending", "cancelled"
    order_date: str

# DATA
customers = [
    Customer(101, "Alice Johnson", "alice@email.com", "New York", "2023-01-15"),
    Customer(102, "Bob Smith", "bob@email.com", "Los Angeles", "2023-06-20"),
    Customer(103, "Charlie Brown", "charlie@email.com", "Chicago", "2024-01-10"),
]

orders = [
    Order(1, 101, "Laptop", 1200.00, "completed", "2024-01-15"),
    Order(2, 101, "Mouse", 25.00, "completed", "2024-01-16"),
    Order(3, 101, "Monitor", 300.00, "pending", "2024-02-01"),
    Order(4, 101, "Keyboard", 80.00, "cancelled", "2024-02-05"),
    Order(5, 102, "Laptop", 1200.00, "completed", "2024-01-20"),
    Order(6, 102, "Headphones", 150.00, "completed", "2024-01-25"),
    Order(7, 102, "Mouse", 25.00, "pending", "2024-02-10"),
    Order(8, 103, "Desk Chair", 400.00, "completed", "2024-02-15"),
]

# HELPER
def get_customer_by_id(customer_id: int) -> Optional[Customer]:
    return next((c for c in customers if c.customer_id == customer_id), None)

# PATTERN 3 - NESTED AGGREGATION
def get_customer_order_history(customer_id:int):
    customer=get_customer_by_id(customer_id)
    if not customer:
        return None
    customer_orders=[o for o in orders if o.customer_id==customer_id]

    grouped=defaultdict(list)
    for order in customer_orders:
        grouped[order.status].append(order)

    order_stats={}
    total_spent=0

    for status, status_orders in grouped.items():
        count=len(status_orders)
        total=sum(o.amount for o in status_orders)
        avg=total/count if count >0 else 0 

        order_stats[status]={
            "orders":status_orders,
            "total":total,
            "count":count,
            "average":avg
        }
        if status =="completed":
            total_spent+=total

    return {
        "customer":customer,
        "order_stats":order_stats,
        "summary":{
            "total_orders":len(customer_orders),
            "total_spent":total_spent,
            "statuses":list(grouped.keys())
        }
    }


# TEST IT
result = get_customer_order_history(101)
if result:
    cust = result['customer']
    print(f"=== CUSTOMER #{cust.customer_id}: {cust.name} ===")
    print(f"Email: {cust.email}")
    print(f"City: {cust.city}")
    print(f"Member Since: {cust.member_since}")
    
    print(f"\n📊 ORDER SUMMARY:")
    print(f"Total Orders: {result['summary']['total_orders']}")
    print(f"Total Spent: ${result['summary']['total_spent']:,.2f}")
    print(f"Order Statuses: {', '.join(result['summary']['statuses'])}")
    
    print(f"\n📦 ORDERS BY STATUS:\n")
    
    for status, stats in result['order_stats'].items():
        print(f"{status.upper()}:")
        print(f"  Count: {stats['count']}")
        print(f"  Total: ${stats['total']:,.2f}")
        print(f"  Average: ${stats['average']:.2f}")
        print(f"  Orders:")
        for order in stats['orders']:
            print(f"    - #{order.order_id}: {order.product} (${order.amount:.2f}) [{order.order_date}]")
        print()

# OUTPUT:
# === CUSTOMER #101: Alice Johnson ===
# Email: alice@email.com
# City: New York
# Member Since: 2023-01-15
#
# 📊 ORDER SUMMARY:
# Total Orders: 4
# Total Spent: $1,525.00
# Order Statuses: completed, pending, cancelled
#
# 📦 ORDERS BY STATUS:
#
# COMPLETED:
#   Count: 2
#   Total: $1,225.00
#   Average: $612.50
#   Orders:
#     - #1: Laptop ($1200.00) [2024-01-15]
#     - #2: Mouse ($25.00) [2024-01-16]
#
# PENDING:
#   Count: 1
#   Total: $300.00
#   Average: $300.00
#   Orders:
#     - #3: Monitor ($300.00) [2024-02-01]
#
# CANCELLED:
#   Count: 1
#   Total: $80.00
#   Average: $80.00
#   Orders:
#     - #4: Keyboard ($80.00) [2024-02-05]