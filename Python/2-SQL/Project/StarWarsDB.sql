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
    series_title TEXT UNIQUE NOT NULL,
    series_seasons INT NOT NULL,
    series_creator TEXT NOT NULL,
    series_startdate DATE NOT NULL,
    series_enddate DATE NOT NULL,
    series_description TEXT,
    series_website TEXT,
    PRIMARY KEY (series_title)
);

CREATE TABLE episodes (
    epi_title TEXT UNIQUE NOT NULL,
    epi_series TEXT UNIQUE NOT NULL references series(series_title),
    epi_season INT NOT NULL,
    epi_airdate DATE NOT NULL,
    epi_description TEXT,
    PRIMARY KEY (epi_title)
);

CREATE TABLE studios (
    studios_name TEXT UNIQUE NOT NULL,
    series_title TEXT UNIQUE NOT NULL references series(series_title),
    studios_address TEXT UNIQUE NOT NULL,
    studios_description TEXT,
    studios_website TEXT UNIQUE NOT NULL,
    PRIMARY KEY (studios_name)
);

CREATE TABLE characters (
    characters_name TEXT UNIQUE NOT NULL,
    characters_part TEXT UNIQUE NOT NULL,
    series_title TEXT UNIQUE NOT NULL references series(series_title),
    epi_title TEXT UNIQUE NOT NULL references episodes(epi_title),
    characters_description TEXT,
    PRIMARY KEY (characters_name)
);

CREATE TABLE actors (
    actors_name TEXT UNIQUE NOT NULL,
    characters_name TEXT UNIQUE NOT NULL references characters(characters_name),
    actors_description TEXT,
    actors_website TEXT UNIQUE NOT NULL,
    PRIMARY KEY (actors_name)
);

---
--- Add foreign key constraints
---

-- ALTER TABLE episodes
-- ADD CONSTRAINT fk_episodes_epi_series
-- FOREIGN KEY (epi_series) 
-- REFERENCES series;
