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
    epi_season INT NOT NULL,
    epi_airdate DATE NOT NULL,
    epi_description TEXT,
    PRIMARY KEY (id)
);

CREATE TABLE series (
    id SERIAL,
    ser_title TEXT UNIQUE NOT NULL,
    ser_seasons INT NOT NULL,
    ser_creator TEXT NOT NULL,
    ser_startdate DATE NOT NULL,
    ser_enddate DATE NOT NULL,
    ser_description TEXT,
    ser_website TEXT,
    PRIMARY KEY (id)
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
    PRIMARY KEY (id)
);

CREATE TABLE actors (
    id SERIAL,
    act_name TEXT UNIQUE NOT NULL,
    act_description TEXT,
    act_website TEXT UNIQUE NOT NULL,
    PRIMARY KEY (id)
);

---
--- Add foreign key constraints
---

ALTER TABLE series
ADD CONSTRAINT fk_series_episodes
FOREIGN KEY (ser_seasons) 
REFERENCES episodes;

ALTER TABLE series
ADD CONSTRAINT fk_series_characters
FOREIGN KEY (ser_seasons) 
REFERENCES characters;

ALTER TABLE series
ADD CONSTRAINT fk_series_actors
FOREIGN KEY (ser_seasons) 
REFERENCES actors;

ALTER TABLE series
ADD CONSTRAINT fk_series_studios
FOREIGN KEY (ser_seasons) 
REFERENCES studios;

ALTER TABLE episodes
ADD CONSTRAINT fk_episodes_characters
FOREIGN KEY (epi_season) 
REFERENCES characters;