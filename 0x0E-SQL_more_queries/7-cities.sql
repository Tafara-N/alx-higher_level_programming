-- A script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa)
-- cities description:
--  id INT unique, auto generated, can’t be null and is a primary key
--  state_id INT, can’t be null and it's FOREIGN KEY references to id of the states table
-- name VARCHAR(256) can’t be null

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id);