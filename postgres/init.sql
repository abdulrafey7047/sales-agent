-- 1. Create Tables
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10, 2)
);

CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    postal_code VARCHAR(20),
    city VARCHAR(50),
    age INT,
    gender VARCHAR(20)
);

CREATE TABLE sales (
    sale_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    product_id INT REFERENCES products(product_id),
    sale_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Temporary table to hold raw CSV data
CREATE TEMP TABLE raw_import (
    first_name TEXT, last_name TEXT, postal_code TEXT, city TEXT, age INT, gender TEXT,
    product_name TEXT, category TEXT, price DECIMAL,
    sale_date TIMESTAMP
);

-- 3. Import from CSV
-- Assumes CSV header: first_name,last_name,postal_code,city,age,gender,product_name,category,price,sale_date
COPY raw_import FROM '/var/lib/postgresql/csv_data/data.csv' WITH (FORMAT csv, HEADER true);

-- 4. Distribute data into normalized tables
INSERT INTO users (first_name, last_name, postal_code, city, age, gender)
SELECT DISTINCT first_name, last_name, postal_code, city, age, gender FROM raw_import;

INSERT INTO products (product_name, category, price)
SELECT DISTINCT product_name, category, price FROM raw_import;

INSERT INTO sales (user_id, product_id, sale_date)
SELECT u.user_id, p.product_id, r.sale_date
FROM raw_import r
JOIN users u ON r.first_name = u.first_name AND r.last_name = u.last_name
JOIN products p ON r.product_name = p.product_name;
