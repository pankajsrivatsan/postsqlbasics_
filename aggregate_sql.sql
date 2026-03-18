-- 1. Create the table
CREATE TABLE IF NOT EXISTS sales_data (
    id SERIAL PRIMARY KEY,
    salesperson VARCHAR(50),
    region VARCHAR(50),
    sale_amount NUMERIC,
    sale_date DATE
);

-- 2. Insert dummy data
INSERT INTO sales_data (salesperson, region, sale_amount, sale_date) VALUES
('Alice', 'North', 100.00, '2023-01-01'),
('Alice', 'North', 200.00, '2023-01-02'),
('Bob', 'South', 150.00, '2023-01-01'),
('Bob', 'South', NULL, '2023-01-03'),      -- NULL sale amount!
('Charlie', 'North', 300.00, '2023-01-01'),
('Alice', 'South', 50.00, '2023-01-04'),
('Charlie', 'North', 100.00, '2023-01-05'),
('Bob', 'South', 400.00, '2023-01-06');




SELECT * FROM sales_data;

--NOW IT'S ABOUT GROUPING
SELECT salesperson,SUM(sale_amount) as total_sales
FROM sales_data
GROUP BY salesperson;


--total sales per salesperson
SELECT region, COUNT(*) as num_transactions
FROM sales_data
GROUP BY region;


