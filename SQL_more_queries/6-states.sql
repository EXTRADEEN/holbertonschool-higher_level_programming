-- creates a new database 'hbtn_0d_usa'
-- create a table 'states' in this database
-- description id=INT unique, auto generated, can’t be null and is a primary key
-- descrioption name=VARCHAR(256) can’t be null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states (
    id INT UNIQUE AUTO_INCREMENT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);