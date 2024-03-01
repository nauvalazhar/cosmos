-- This is an extended SQL example intended to test syntax highlighting, overflow, and understanding of SQL commands.

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (username, email) VALUES ('user1', 'user1@example.com'), ('user2', 'user2@example.com');

SELECT * FROM users;

UPDATE users SET username = 'updatedUser1' WHERE id = 1;

DELETE FROM users WHERE id = 2;

-- Join example
SELECT users.username, orders.amount
FROM users
INNER JOIN orders ON users.id = orders.user_id
WHERE orders.amount > 100;
