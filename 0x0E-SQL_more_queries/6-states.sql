-- Script creates table unique_id
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT AUTO_INCREMENT UNIQUE, name VARCHAR(256) NOT NULL, PRIMARY KEY (id));
