-- cat StarWarsDB.sql | docker exec -i pg_container psql
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

CREATE TABLE series (
    ser_title TEXT UNIQUE NOT NULL,
    ser_seasons INT NOT NULL,
    ser_creator TEXT NOT NULL,
    ser_startdate DATE NOT NULL,
    ser_enddate DATE NOT NULL,
    ser_description TEXT,
    ser_website TEXT,
    PRIMARY KEY (ser_title)
);

CREATE TABLE episodes (
    epi_title TEXT UNIQUE NOT NULL,
    epi_series TEXT UNIQUE NOT NULL references series(ser_title),
    epi_season INT NOT NULL,
    epi_airdate DATE NOT NULL,
    epi_description TEXT,
    PRIMARY KEY (epi_title)
);

CREATE TABLE studios (
    stu_name TEXT UNIQUE NOT NULL,
    ser_title TEXT UNIQUE NOT NULL references series(ser_title),
    stu_address TEXT UNIQUE NOT NULL,
    stu_description TEXT,
    stu_website TEXT UNIQUE NOT NULL,
    PRIMARY KEY (stu_name)
);

CREATE TABLE characters (
    cha_name TEXT UNIQUE NOT NULL,
    cha_part TEXT UNIQUE NOT NULL,
    ser_title TEXT UNIQUE NOT NULL references series(ser_title),
    epi_title TEXT UNIQUE NOT NULL references episodes(epi_title),
    cha_description TEXT,
    PRIMARY KEY (cha_name)
);

CREATE TABLE actors (
    act_name TEXT UNIQUE NOT NULL,
    cha_name TEXT UNIQUE NOT NULL references characters(cha_name),
    act_description TEXT,
    act_website TEXT UNIQUE NOT NULL,
    PRIMARY KEY (act_name)
);

---
--- Add foreign key constraints
---

-- ALTER TABLE episodes
-- ADD CONSTRAINT fk_episodes_epi_series
-- FOREIGN KEY (epi_series) 
-- REFERENCES series;
