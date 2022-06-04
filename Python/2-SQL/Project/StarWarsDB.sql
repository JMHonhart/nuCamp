-- kill other connections
SELECT pg_terminate_backend(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE pg_stat_activity.datname = 'starwars_db' AND pid <> pg_backend_pid();

-- (re)create the database
DROP DATABASE IF EXISTS starwars_db;
CREATE DATABASE starwars_db;

-- connect via psql
\c starwars_db

-- database configuration
SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET default_tablespace = '';
SET default_with_oids = false;


---
--- CREATE tables
---

CREATE TABLE episodes (
    id SERIAL,
    title TEXT UNIQUE NOT NULL,
    season TEXT UNIQUE NOT NULL,
    airdate DATE NOT NULL,
    description TEXT,
    PRIMARY KEY (id)
);

CREATE TABLE series (
    id SERIAL,
    title TEXT UNIQUE NOT NULL,
    creator TEXT UNIQUE NOT NULL,
    startdate DATE NOT NULL,
    enddate DATE NOT NULL,
    website TEXT,
    PRIMARY KEY (id)
);

CREATE TABLE studios (
    id SERIAL,
    name TEXT UNIQUE NOT NULL,
    address TEXT UNIQUE NOT NULL,
    website TEXT UNIQUE NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE characters (
    id SERIAL,
    name TEXT UNIQUE NOT NULL,
    role TEXT UNIQUE NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE actors (
    id SERIAL,
    name TEXT UNIQUE NOT NULL,
    website TEXT UNIQUE NOT NULL,
    PRIMARY KEY (id)
);

---
--- Add foreign key constraints
---

-- PRODUCTS

-- ALTER TABLE products
-- ADD CONSTRAINT fk_products_categories 
-- FOREIGN KEY (category_id) 
-- REFERENCES categories (id);


-- TODO create more constraints here...

-- ALTER TABLE orders
-- ADD CONSTRAINT fk_orders_customers
-- FOREIGN KEY (customer_id) 
-- REFERENCES customers;

-- ALTER TABLE orders
-- ADD CONSTRAINT fk_orders_employees
-- FOREIGN KEY (employee_id) 
-- REFERENCES employees;
