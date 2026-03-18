CREATE TABLE customers (
    id    SERIAL PRIMARY KEY,
    name  VARCHAR(100),
    city  VARCHAR(100)
);

CREATE TABLE orders (
    id          SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(id),
    product     VARCHAR(100),
    amount      NUMERIC
);

INSERT INTO customers (name, city) VALUES
('alice',   'mumbai'),
('bob',     'delhi'),
('carol',   'bangalore'),
('dave',    'chennai');

INSERT INTO orders (customer_id, product, amount) VALUES
(1, 'laptop',   75000),
(1, 'mouse',     1500),
(2, 'phone',    45000),
(3, 'tablet',   30000),
(3, 'keyboard',  2000),
(3, 'monitor',  15000);
```

Notice — dave has **no orders.** That's intentional.

---

## What We Have
```
customers table          orders table
───────────────          ────────────────────────
id | name  | city        id | customer_id | product  | amount
1  | alice | mumbai       1 | 1           | laptop   | 75000
2  | bob   | delhi        2 | 1           | mouse    |  1500
3  | carol | bangalore    3 | 2           | phone    | 45000
4  | dave  | chennai      4 | 3           | tablet   | 30000
                          5 | 3           | keyboard |  2000
                          6 | 3           | monitor  | 15000


SELECT c.name, c.city, SUM(o.amount) AS total_amount, COUNT(o.product) 
FROM customers c
JOIN orders o  ON c.id = o.customer_id
GROUP BY c.name,c.city
ORDER BY total_amount DESC;

