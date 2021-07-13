-- script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.
-- If table of database already exists, script does not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
       id INT NOT NULL AUTO_INCREMENT UNIQUE,
       state_id INT NOT NULL, FOREIGN KEY (statesID) REFERENCES hbtn_0d_usa.states (statesID),
       name VARCHAR(256) NOT NULL,
       PRIMARY KEY (ID)
);
