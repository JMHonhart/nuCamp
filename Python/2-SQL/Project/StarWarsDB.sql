-- kill other connections
SELECT pg_terminate_backend(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE pg_stat_activity.datname = 'starwars_db' AND pid <> pg_backend_pid();

-- (re)create the database
DROP DATABASE IF EXISTS starwars_db;
CREATE DATABASE starwars_db;

-- connect via psql
\c starwars_db; 

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
    epi_title TEXT UNIQUE NOT NULL,
    epi_season INT UNIQUE NOT NULL,
    epi_airdate DATE NOT NULL,
    epi_description TEXT,
    PRIMARY KEY (epi_title)
);

CREATE TABLE series (
    id SERIAL,
    ser_title TEXT UNIQUE NOT NULL,
    ser_creator TEXT UNIQUE NOT NULL,
    ser_startdate DATE NOT NULL,
    ser_enddate DATE NOT NULL,
    ser_description TEXT,
    ser_website TEXT,
    PRIMARY KEY (ser_title)
);

CREATE TABLE studios (
    id SERIAL,
    stu_name TEXT UNIQUE NOT NULL,
    stu_address TEXT UNIQUE NOT NULL,
    stu_description TEXT,
    stu_website TEXT UNIQUE NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE characters (
    id SERIAL,
    cha_name TEXT UNIQUE NOT NULL,
    cha_part TEXT UNIQUE NOT NULL,
    cha_description TEXT,
    PRIMARY KEY (cha_name)
);

CREATE TABLE actors (
    id SERIAL,
    act_name TEXT UNIQUE NOT NULL,
    act_description TEXT,
    act_website TEXT UNIQUE NOT NULL,
    PRIMARY KEY (act_name)
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