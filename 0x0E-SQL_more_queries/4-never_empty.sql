--  script that creates the table id_not_null on your MySQL server.
-- If the table already exists, script does not fail.
CREATE TABLE IF NOT EXISTS id_not_null (id INT(1),name VARCHAR(256));
