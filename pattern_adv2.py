from dataclasses import dataclass
from typing import Optional

# ======================
# DATA MODELS
# ======================

@dataclass
class Customer:
    customer_id: int
    name: str
    email: str
    company: str

@dataclass
class Product:
    product_id: int
    name: str
    price: float
    category: str

@dataclass
class Invoice:
    invoice_id: int
    customer_id: int
    invoice_date: str
    due_date: str
    status: str

@dataclass
class InvoiceItem:
    item_id: int
    invoice_id: int
    product_id: int
    quantity: int
    discount: float


# ======================
# DATA
# ======================

customers = [
    Customer(1, "TechCorp", "contact@techcorp.com", "TechCorp Inc."),
    Customer(2, "DesignCo", "hello@designco.com", "DesignCo LLC"),
]

products = [
    Product(1, "Website Development", 5000.00, "Services"),
    Product(2, "Logo Design", 1000.00, "Design"),
    Product(3, "SEO Optimization", 2000.00, "Services"),
    Product(4, "Social Media Management", 1500.00, "Marketing"),
]

invoices = [
    Invoice(1, 1, "2025-01-01", "2025-01-31", "paid"),
    Invoice(2, 2, "2025-01-15", "2025-02-15", "pending"),
]

invoice_items = [
    InvoiceItem(1, 1, 1, 1, 0.0),
    InvoiceItem(2, 1, 3, 1, 0.1),
    InvoiceItem(3, 2, 2, 2, 0.0),
    InvoiceItem(4, 2, 4, 3, 0.15),
]
def get_customer_by_id(customer_id:int)->Optional[Customer]:
    return next((c for c in customers if c.customer_id==customer_id),None)
def get_product_by_id(product_id:int)->Optional[Product]:
    return next((i for i in products if i.product_id==product_id),None)
def get_invoice_by_id(invoice_id:int)->Optional[Invoice]:
    return next((p for p in invoices if p.invoice_id==invoice_id ),None)

#main function
def get_invoice_details(invoice_id:int):
    invoice=get_invoice_by_id(invoice_id)
    if not invoice:
        return None
    
    customer=get_customer_by_id(invoice.customer_id)
    items=(item for item in invoice_items if item.invoice_id==invoice_id)

    line_items=[]
    invoice_subtotal=0
    for item in items:
        product=get_product_by_id(item.product_id)
        if not product:
            continue
        unit_price=product.price
        item_subtotal=unit_price*item.quantity*(1-item.discount)
        line_items.append({
            "product_name":product.name,
            "category":product.category,
            "unit_price":unit_price,
            "quantity":item.quantity,
            "discount_pct":item.discount*100,
            "subtotal":item_subtotal
        })
        invoice_subtotal+=item_subtotal
        
    tax=invoice_subtotal*0.08
    total=invoice_subtotal+tax
    return{
        "invoice":invoice,
        "customer":customer,
        "line_items":line_items,
        "summary":{
            "subtotal":invoice_subtotal,
            "tax":tax,
            "total":total
        }
    }

result = get_invoice_details(1)

if result:
    print(f"=== INVOICE #{result['invoice'].invoice_id} ===")

    print("\nCustomer:")
    print(f"  Name: {result['customer'].name}")
    print(f"  Email: {result['customer'].email}")
    print(f"  Company: {result['customer'].company}")

    print("\nInvoice Info:")
    print(f"  Date: {result['invoice'].invoice_date}")
    print(f"  Due Date: {result['invoice'].due_date}")
    print(f"  Status: {result['invoice'].status}")

    print("\nLine Items:")
    for i, item in enumerate(result['line_items'], 1):
        print(f"  {i}. {item['product_name']} ({item['category']})")
        print(f"     Qty: {item['quantity']} × ${item['unit_price']:,.2f} "
              f"({item['discount_pct']:.0f}% discount) = ${item['subtotal']:,.2f}")
        print()

    print("Summary:")
    print(f"  Subtotal: ${result['summary']['subtotal']:,.2f}")
    print(f"  Tax (8%): ${result['summary']['tax']:,.2f}")
    print(f"  Total: ${result['summary']['total']:,.2f}")


