-- script that creates the table force_name on your MySQL server.
-- If the table already exists, script does not fail.
CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);
