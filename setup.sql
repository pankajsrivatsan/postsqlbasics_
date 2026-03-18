CREATE TABLE IF NOT EXISTS products(
    id          SERIAL PRIMARY KEY,
    name        VARCHAR(100),
    category    VARCHAR(50),
    price       NUMERIC,
    stock       INT
);

INSERT INTO products (name, category,price, stock) VALUES
('APPLE',   'FRUIT', 1.50, 100),
('BANANA',  'FRUIT',0.75,200),
('CARROT',  'VEGETABLES',0.90,150),
('BROCCOLI', 'VEGETABLES',1.20, 150),
('MANGO',    'FRUIT', 2.50, 60),
('SPINACH',   'VEGETABLES', 1.80, 90),
('WATERMELON', 'FRUIT', 5.00, 30);

SELECT category, SUM(price*stock) AS total_val
FROM products
GROUP BY category;

SELECT category, SUM(stock) AS total_stock
FROM products
GROUP BY category
ORDER BY total_stock DESC;

SELECT category, MAX(price) AS expen_item
FROM products
GROUP BY category
HAVING MAX(price) >2.00;

SELECT COUNT(*) AS products_ab_avg
FROM products
WHERE price> (SELECT AVG(price) FROM products);

