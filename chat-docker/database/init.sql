CREATE DATABASE IF NOT EXISTS chatdb;
USE chatdb;

CREATE TABLE messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    content TEXT,
    time DATETIME
);
