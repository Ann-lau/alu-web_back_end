-- TABLE users:
-- id: Integer, auto increment, primary key
-- email: String (255), unique, not null
-- name: String (255)
-- country: Enum ('US', 'CO', 'TN') with default 'US', not null

CREATE TABLE IF NOT EXISTS users (
       id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
       email VARCHAR(255) NOT NULL UNIQUE,
       name VARCHAR(255),
       country ENUM ('US', 'CO', 'TN') NOT NULL
);
