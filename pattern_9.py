from dataclasses import dataclass

@dataclass
class Order:
    id: int
    customer: str
    total: float
    status: str
    items_count: int

orders: list[Order] = [
    Order(1, "Alice", 150.00, "completed", 3),
    Order(2, "Bob", 250.00, "pending", 5),
    Order(3, "Charlie", 75.00, "completed", 2),
    Order(4, "Dana", 500.00, "completed", 8),
    Order(5, "Eve", 120.00, "cancelled", 4),
    Order(6, "Frank", 300.00, "pending", 6),
    Order(7, "Grace", 450.00, "completed", 7),
    Order(8, "Henry", 80.00, "pending", 2),
    Order(9, "Ivy", 200.00, "completed", 4),
    Order(10, "Jack", 350.00, "pending", 5),
    Order(11, "Kate", 280.00, "completed", 6),
    Order(12, "Leo", 90.00, "cancelled", 3),
    Order(13, "Mia", 400.00, "completed", 7),
    Order(14, "Noah", 175.00, "pending", 4),
    Order(15, "Olivia", 310.00, "completed", 5)
]

def get_revenue_calculations():
    "calculate revenue metrics"
    
    #step:1 all orders calculations:
    total_orders=len(orders)
    total_revenue=sum(o.total for o in orders)
    average_order=total_revenue/ total_orders if total_orders >0 else 0 
    highest_order= max(o.total for o in orders)
    lowest_order=min(o.total for o in orders)


    #step 2: filter then calculate
    completed=[o for o in orders if o.status == "completed"]
    pending=[o for o in orders if o.status == "pending"]
    cancelled=[o for o in orders if o.status == "cancelled"]

    #revenue by status 
    completed_revenue= sum(o.total for o in completed)
    pending_revenue= sum(o.total for o in pending)
    cancelled_revenue=sum(o.total for o in cancelled)

    #average by status 
    completed_average=completed_revenue/len(completed) if completed else 0
    pending_avg=pending_revenue/len(pending) if pending else 0 

    #step 3: items calculations
    total_items= sum(o.items_count for o in orders)
    avg_items= total_items/total_orders if total_orders >0 else 0 

    return {
        "overall": {
            "total_orders":total_orders,
            "total_revenue":round(total_revenue,2),
            "average_orders":round(average_order,2),
            "highest_orders":highest_order,
            "lowest_orders":lowest_order
        },
        "by_status":{
            "completed_revenue":round(completed_revenue,2),
            "pending_revenue":round(pending_revenue,2),
            "cancelled_revenue":round(cancelled_revenue,2),
            "completed_avg":round(completed_average,2),
            "pending_avg":round(pending_avg,2),
        },
        "items":{
            "total_items_sold":total_items,
            "avg_items_per_order":round(avg_items,1)
        }
    }

calc=get_revenue_calculations()
print(calc)