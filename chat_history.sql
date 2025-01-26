CREATE DATABASE chatbot;

USE chatbot;

CREATE TABLE chat_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    role VARCHAR(10),
    content TEXT
);
