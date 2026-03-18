from dataclasses import dataclass

@dataclass
class Product:
    id: int
    name: str
    category: str
    price: float
    stock: int
    rating: float

products: list[Product] = [
    Product(1, "Laptop", "Electronics", 999.99, 15, 4.8),
    Product(2, "Mouse", "Electronics", 29.99, 120, 4.5),
    Product(3, "Desk", "Furniture", 299.00, 8, 3.8),
    Product(4, "Chair", "Furniture", 199.00, 25, 4.7),
    Product(5, "Monitor", "Electronics", 349.99, 30, 4.6),
    Product(6, "Keyboard", "Electronics", 89.99, 80, 4.1),
    Product(7, "Bookshelf", "Furniture", 149.00, 12, 4.0),
    Product(8, "Webcam", "Electronics", 79.99, 45, 3.9),
    Product(9, "Lamp", "Furniture", 45.00, 60, 4.3),
    Product(10, "Headphones", "Electronics", 159.99, 35, 4.9),
    Product(11, "Sofa", "Furniture", 799.00, 5, 4.4),
    Product(12, "Router", "Electronics", 129.99, 50, 4.0),
    Product(13, "Table", "Furniture", 399.00, 10, 4.2),
    Product(14, "Tablet", "Electronics", 449.99, 20, 4.5),
    Product(15, "Cabinet", "Furniture", 249.00, 7, 3.7),
    Product(16, "Speaker", "Electronics", 199.99, 40, 4.6),
    Product(17, "Ottoman", "Furniture", 129.00, 18, 4.1),
    Product(18, "Microphone", "Electronics", 119.99, 25, 4.7),
    Product(19, "Rug", "Furniture", 179.00, 14, 3.9),
    Product(20, "Charger", "Electronics", 39.99, 100, 4.2)
]

# YOUR TASK: Write this function
def get_product_stats():
    total_products=len(products)

    #step 2by_category
    electronics=len([p for p in products if p.category=="Electronics"])
    furniture=len([p for p in products if p.category=="Furniture"])
    electronics_percent=(electronics/total_products*100) if total_products>0 else 0 
    furniture_percent=(furniture/total_products*100) if total_products>0 else 0 


    #step 3 by stock status
    in_stock=len([p for p in products if p.stock >0])
    low_stock=len([p for p in products if p.stock <=10])
    out_of_stock=len([p for p in products if p.stock ==0])

    #step 4 by rating 
    excellent=len([p for p in products if p.rating >=4.5])
    good=len([p for p in products if 4.0 <=p.rating <4.5])
    average=len([p for p in products if p.rating <4.0])

    #step 5 by price tier:
    premium=len([p for p in products if p.price >=300])
    mid_range=len([p for p in products if 100 <= p.price <299])
    budget=len([p for p in products if p.price <100])


    return {
        "all_products":total_products,

        "by_stock":{
            "in_stock":in_stock,
            "low_stock":low_stock,
            "out_of_stock":out_of_stock
        },
        "by_rating":{
            "excellent":excellent,
            "good":good,
            "average":average,
        
        },
        "by_price_tier":{
            "premium":premium,
            "mid_range":mid_range,
            "budget":budget

        },
        "by_category":{
            "percentage_electronics":round(electronics_percent,1),
            "percentage_furniture":round(furniture_percent,1),
            "electronics":electronics,
            "furniture":furniture
        }    

        }

stats= get_product_stats()

print(stats)
