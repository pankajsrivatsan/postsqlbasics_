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
    Product(1, "Laptop", "Electronics", 999.99, 15, 4.5),
    Product(2, "Mouse", "Electronics", 25.50, 120, 4.2),
    Product(3, "Desk", "Furniture", 299.00, 8, 3.8),
    Product(4, "Chair", "Furniture", 199.00, 25, 4.7),
    Product(5, "Monitor", "Electronics", 349.99, 30, 4.6),
    Product(6, "Keyboard", "Electronics", 75.00, 80, 4.1),
    Product(7, "Bookshelf", "Furniture", 149.00, 12, 4.0),
    Product(8, "Webcam", "Electronics", 89.99, 45, 3.9),
    Product(9, "Lamp", "Furniture", 45.00, 60, 4.3),
    Product(10, "Headphones", "Electronics", 159.99, 35, 4.8),
    Product(11, "Sofa", "Furniture", 799.00, 5, 4.4),
    Product(12, "Router", "Electronics", 129.99, 50, 4.0),
    Product(13, "Table", "Furniture", 399.00, 10, 4.2),
    Product(14, "Tablet", "Electronics", 449.99, 20, 4.5),
    Product(15, "Cabinet", "Furniture", 249.00, 7, 3.7)
]
def get_products_sorted(sort_by:str, order="asc")-> list[Product]:
    must_reverse=order=="desc"
    result=sorted(products, key=lambda p:getattr(p, sort_by), reverse=must_reverse)
    return result

def get_top_rated(n)-> list[Product]:
    sorted_products=sorted(products, key=lambda p:p.rating, reverse=True)
    return sorted_products[:n]

def get_cheapest(n)-> list[Product]:
    sorted_products=sorted(products, key=lambda p: p.price, reverse=False)
    return sorted_products[:n]

print("test1")
print([f"{p.name}- {p.price}" for p in get_products_sorted("price", "desc")])

print("test2")
print([f"{p.name}- {p.rating}" for p in get_products_sorted("rating","desc")])

print("test3")
print([f"{p.name}" for p in get_products_sorted("name", "asc")])

print("test4")
print([f"{p.name}- {p.rating}" for p in get_top_rated(5)])

print("test5")
print([f"{p.name} - {p.price}" for p in get_cheapest(3)])

