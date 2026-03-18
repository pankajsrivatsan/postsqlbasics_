from dataclasses import dataclass
from collections import defaultdict

@dataclass
class Order:
    order_id: int
    customer_id: int
    region: str
    amount: float
    status: str

orders = [
    Order(1, 101, "North", 150, "completed"),
    Order(2, 102, "South", 200, "completed"),
    Order(3, 101, "North", 100, "completed"),
    Order(4, 103, "North", 300, "cancelled"),
    Order(5, 102, "South", 250, "completed"),
]

def get_region_stats():
    grouped=defaultdict(list)
    for order in orders:
        grouped[order.region].append(order)

    result={}
    for region, region_orders in grouped.items():
        completed=[ o for o in region_orders if o.status =="completed"]
        result[region]={
            "total_orders":len(region_orders),
            "total_revenue":sum(o.amount for o in completed),
            "completed_orders":len(completed),
            "unique_customers":len(set(o.customer_id for o in region_orders))
        }
    return result




   

result=get_region_stats()
for region, stats in result.items():
    print(f"\n{region}")
    print(f"total orders: {stats['total_orders']}")
    print(f"completed: {stats['completed_orders']}")
    print(f"revenue: {stats['total_revenue']:.2f}")
    print(f"unique customers: {stats['unique_customers']}")
