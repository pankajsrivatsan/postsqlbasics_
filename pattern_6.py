from dataclasses import dataclass

@dataclass
class Product:
    id: int
    name: str
    price: float

# 25 products
products: list[Product] = [
    Product(1, "Laptop", 999.99),
    Product(2, "Mouse", 25.50),
    Product(3, "Keyboard", 75.00),
    Product(4, "Monitor", 349.99),
    Product(5, "Webcam", 89.99),
    Product(6, "Headphones", 159.99),
    Product(7, "Desk", 299.00),
    Product(8, "Chair", 199.00),
    Product(9, "Lamp", 45.00),
    Product(10, "Router", 129.99),
    Product(11, "Speaker", 79.99),
    Product(12, "Microphone", 119.99),
    Product(13, "Cable", 15.99),
    Product(14, "Adapter", 29.99),
    Product(15, "Stand", 49.99),
    Product(16, "Tablet", 449.99),
    Product(17, "Phone", 699.99),
    Product(18, "Charger", 39.99),
    Product(19, "Case", 19.99),
    Product(20, "Bag", 59.99),
    Product(21, "Dock", 199.99),
    Product(22, "Hub", 89.99),
    Product(23, "Drive", 149.99),
    Product(24, "Card", 99.99),
    Product(25, "Battery", 49.99)
]

def get_products_paginated(page:int=1, per_page:int=10):
    """
    args:
    page:page number(starts from1 )
    per_page:items per page(default to 10)

    returns:
    dictionary with items and metadata

    """
    #step:1
    start=(page-1)*per_page
    end=start+per_page

    items=products[start:end]
    total_items=len(products)
    total_pages=(total_items+per_page-1)//per_page

    return{
        "items":items,
        "page":page,
        "per_page":per_page,
        "total_items":total_items,
        "total_pages":total_pages,
        "has_next":page<total_pages,
        "has_prev":page>1

    }
print("test1")
result=get_products_paginated(page=1,per_page=10)
print(f"items: {[p.name for p in result['items'][:4]]}")

print("test2")
result=get_products_paginated(page=1, per_page=10)
print(f"items: {[p.name for p in result['items'][:4]]}")
