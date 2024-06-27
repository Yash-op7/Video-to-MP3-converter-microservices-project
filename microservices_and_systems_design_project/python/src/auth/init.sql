-- -- create a db called auth which will be the db for our auth service

-- CREATE USER 'auth_user'@'localhost' IDENTIFIED BY 'Aauth123';    -- this is the user which will use our db, different from the use that will login to our app

-- CREATE DATABASE auth;

-- GRANT ALL PRIVILEGES ON auth.* TO 'auth_user'@'locahost';   -- grant access to user that we created on all tables in the auth database

-- USE auth;

-- CREATE TABLE user (
--     id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
--     email VARCHAR(255) NOT NULL,
--     password VARCHAR(255) NOT NULL
-- );

-- INSERT INTO user (email, password) VALUES ('yash@email.com', 'Admin123');

CREATE USER 'auth_user'@'localhost' IDENTIFIED BY 'Auth123';

CREATE DATABASE auth;

GRANT ALL PRIVILEGES ON auth.* TO 'auth_user'@'localhost';

USE auth;

CREATE TABLE user (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(255) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL
);

INSERT INTO user (email, password) VALUES ('yash@email.com', 'Admin123');

  



