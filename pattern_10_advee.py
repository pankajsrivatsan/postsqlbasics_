from dataclasses import dataclass
from collections import defaultdict

@dataclass
class Order:
    order_id: int
    product: str
    quantity: int
    price: float
    status: str  # "pending", "completed", "cancelled"

orders = [
    Order(1, "Laptop", 1, 1200, "completed"),
    Order(2, "Mouse", 5, 25, "completed"),
    Order(3, "Keyboard", 2, 80, "pending"),
    Order(4, "Monitor", 1, 300, "completed"),
    Order(5, "Laptop", 1, 1200, "cancelled"),
    Order(6, "Mouse", 3, 25, "pending"),
    Order(7, "Keyboard", 1, 80, "completed"),
]
def analyzee_by_status():
    groups=defaultdict(list)
    for order in orders:
        groups[order.status].append(order)

    result={}
    for status ,status_orders in groups.items():
        result[status]={
            "highest_val":max(o.price for o in status_orders)
        }
    return result
result = analyzee_by_status()
for status, stats in result.items():
    print(f"\n{status}:")
    print(f"{stats['highest_val']}")