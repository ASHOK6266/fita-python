DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS lists;

CREATE TABLE users(
  email  VARCHAR(355) UNIQUE NOT NULL,
  firstname VARCHAR(50) NOT NULL,
  lastname VARCHAR(50) NOT NULL,
  password VARCHAR(355) NOT NULL,
  age INT NOT NULL
);

CREATE TABLE lists(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title VARCHAR(355) NOT NULL,
  body VARCHAR(1000) NOT NULL,
);