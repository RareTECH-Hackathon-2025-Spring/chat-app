
CREATE USER 'testuser' IDENTIFIED BY 'testuser';
CREATE DATABASE chatapp;
USE chatapp
GRANT ALL PRICILEGES ON chatapp.* TO 'testuser';

CREATE TABLE teams (
    id INT AUTO_INCReMENT PRIMARY KEY,
    teamname VARCHAR(50) UNIQUE, NOT NULL,
);

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(50) UNIQUE, NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    team_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    FOREIGN KEY (team_id) PREFERENCES teams(id),
);

CREATE TABLE channels (
    id INT AUTO_INCREMENT PRIMARY KEY,
    channel_name VARCHAR(100) NOT NULL,
    description TEXT, NULL,
    created_by INT NOT NULL,
    FOREIGN KEY (created_by) REFERENCES users(id),
);

CREATE TABLE channel_members (
    id INT AUTO_INCREMENT PRIMARY KEY,
    
);

CREATE TABLE message (
    id INT AUTO_INCREMENT PRIMARY KEY,
);

CREATE TABLE worktime (
    id INT AUTO_INCREMENT PRIMARY KEY,

);


