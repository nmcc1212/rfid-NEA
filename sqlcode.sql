/* Iteration 1*/

CREATE TABLE card_states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    card_id VARCHAR(255) NOT NULL,
    binary_value TINYINT(1) NOT NULL,
    timestamp DATETIME NOT NULL
);


/* Iteration 2*/

ALTER TABLE card_states
ADD COLUMN name VARCHAR(255);
