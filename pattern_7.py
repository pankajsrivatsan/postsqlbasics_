from dataclasses import dataclass

@dataclass
class Product:
    id: int
    name: str
    category: str
    price: float
    stock: int
    rating: float

# 30 products across 3 categories
products: list[Product] = [
    Product(1, "Laptop Pro", "Electronics", 1299.99, 15, 4.8),
    Product(2, "Wireless Mouse", "Electronics", 29.99, 120, 4.5),
    Product(3, "Mechanical Keyboard", "Electronics", 89.99, 80, 4.7),
    Product(4, "4K Monitor", "Electronics", 399.99, 30, 4.6),
    Product(5, "USB Webcam", "Electronics", 79.99, 45, 4.2),
    Product(6, "Bluetooth Headphones", "Electronics", 199.99, 35, 4.9),
    Product(7, "Gaming Mouse", "Electronics", 59.99, 60, 4.4),
    Product(8, "Laptop Stand", "Electronics", 34.99, 90, 4.3),
    Product(9, "HDMI Cable", "Electronics", 12.99, 200, 4.1),
    Product(10, "Power Bank", "Electronics", 49.99, 70, 4.5),
    
    Product(11, "Office Desk", "Furniture", 299.99, 12, 4.7),
    Product(12, "Ergonomic Chair", "Furniture", 249.99, 25, 4.8),
    Product(13, "Bookshelf", "Furniture", 149.99, 18, 4.4),
    Product(14, "Table Lamp", "Furniture", 39.99, 55, 4.2),
    Product(15, "Filing Cabinet", "Furniture", 189.99, 8, 4.3),
    Product(16, "Standing Desk", "Furniture", 449.99, 10, 4.9),
    Product(17, "Storage Unit", "Furniture", 199.99, 15, 4.5),
    Product(18, "Computer Chair", "Furniture", 179.99, 20, 4.6),
    Product(19, "Coat Rack", "Furniture", 49.99, 30, 4.0),
    Product(20, "Side Table", "Furniture", 89.99, 22, 4.1),
    
    Product(21, "Notebook Set", "Stationery", 15.99, 100, 4.3),
    Product(22, "Pen Collection", "Stationery", 24.99, 150, 4.5),
    Product(23, "Sticky Notes", "Stationery", 8.99, 200, 4.2),
    Product(24, "Desk Organizer", "Stationery", 19.99, 80, 4.4),
    Product(25, "Paper Clips", "Stationery", 5.99, 300, 4.0),
    Product(26, "Stapler", "Stationery", 12.99, 120, 4.3),
    Product(27, "Markers Set", "Stationery", 18.99, 90, 4.6),
    Product(28, "Calculator", "Stationery", 29.99, 60, 4.7),
    Product(29, "Folder Pack", "Stationery", 14.99, 110, 4.1),
    Product(30, "Tape Dispenser", "Stationery", 9.99, 140, 4.2)
]

def search_products(
        category:str=None,
        min_price:float=None,
        max_price:float=None,
        min_rating:float=None,
        min_stock:int=None,

        sort_by:str="id",
        order:str="asc",

        page:int=1,
        per_page:int=10
):
    results=products

    if category:
        results=[p for p in results if p.category == category]

    if min_price is not None:
        results=[p for p in results if p.price >=min_price]

    if max_price is not None:
        results = [p for p in results if p.price <= max_price]

    
    if min_rating is not None:
        results=[p for p in results if p.rating>=min_rating]

    if min_stock is not None:
        results=[p for p in results if p.stock >= min_stock]
    if not hasattr(Product, sort_by):
        sort_by = "id"

    #sort results (day5)
    reverse =order=="desc"
    results=sorted(results, key=lambda p:getattr(p, sort_by),reverse=reverse)


    #calculate pagination
    total_items=len(results)
    total_pages=(total_items+per_page-1) //per_page

    #actual pagination
    start=(page-1) * per_page
    end=start +per_page
    items=results[start:end]

    #return complete response

    return{
        "items":items,
        "page":page,
        "per_page":per_page,
        "total_items":total_items,
        "total_pages":total_pages,
        "has_next":page<total_pages,
        "has_prev":page>1,

        #filters (applied(so users know what is active ))
        "filters":{
            "category":category,
            "min_price":min_price,
            "max_price":max_price,
            "min_rating":min_rating,
            "min_stock":min_stock,
            "sort_by":sort_by,
            "order":order
        }
    }
def get_products_by_id(product_id:int)-> Product|None:
    for product in products:
        if product.id== product_id:
            return product
        
    return None

print("test1")
result=search_products(category="Electronics",per_page=5)
print(f"found{result['total_items']} Electronics")
print(f"page{result['page']} of {result['total_pages']}")
print("products:")
for p in result['items']:
    print(f". {p.name}- {p.price} - {p.rating}")

print("test2")
result=search_products(
    category="Furniture",
    min_price=100,
    max_price=300,
    sort_by="price",
    per_page=5
)
print(f"found {result['total_items']}")
print("test3")
result=search_products(
    category="Electronics",
    min_price=50,
    max_price=500,
    min_rating=4.5,
    sort_by="rating",
    order="desc",
    page=1,
    per_page=3
)

print(f"filters: Electronics, 50-500, rating > 4.5")
print(f"found {result['total_items']} matching products")
print(f"showing pages{result['page']}of  {result['total_pages']}")
print("products")
for p in result['items']:
    print(f".{p.name}- {p.rating} - {p.stock}")

print("test4")
product=get_products_by_id(6)
if product:
    print(f"found: {product.name}")
    print(f"category: {product.category}")
    print(f"price: {product.price}")
    print(f"rating:{product.rating}")

else:
    print("not found")

print("test5")
result=search_products(
    category="Stationery",
    sort_by="price",
    order="asc",
    page=2,
    per_page=3
)
print(f"Stationery - page {result['page']} fo {result['total_pages']}")
print(f"navigation: {'prev' if result['has_prev'] else ''} | { 'next' if result['has_next'] else 'last page'}")
for p in result['items']:
    print(f"{p.name} - {p.price}")
