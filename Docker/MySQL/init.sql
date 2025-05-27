-- （開発時のみの実装）すでに存在する場合は削除
DROP DATABASE chatapp;
DROP USER 'testuser';

CREATE DATABASE IF NOT EXISTS chatapp;
CREATE USER IF NOT EXISTS 'testuser'@'%' IDENTIFIED BY 'testuser';
GRANT ALL PRIVILEGES ON chatapp.* TO 'testuser'@'%';
FLUSH PRIVILEGES;
USE chatapp;

-- CREATE USER 'testuser' IDENTIFIED BY 'testuser';
-- CREATE DATABASE chatapp;
-- GRANT ALL PRIVILEGES ON chatapp.* TO 'testuser';
-- USE chatapp;

CREATE TABLE teams (
    id INT AUTO_INCREMENT PRIMARY KEY,
    teamname VARCHAR(50) UNIQUE NOT NULL,
    url_token VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    team_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (team_id) REFERENCES teams(id)
);

CREATE TABLE channels (
    id INT AUTO_INCREMENT PRIMARY KEY,
    channel_name VARCHAR(100) NOT NULL,
    channel_description TEXT NOT NULL,
    team_id INT NOT NULL,
    created_by INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (team_id) REFERENCES teams(id),
    FOREIGN KEY (created_by) REFERENCES users(id)
);

CREATE TABLE channel_members (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    channel_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (channel_id) REFERENCES channels(id)
);

CREATE TABLE messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    content TEXT NOT NULL,
    user_id INT NOT NULL,
    channel_id INT NOT NULL,
    team_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (channel_id) REFERENCES channels(id),
    FOREIGN KEY (team_id) REFERENCES teams(id)
);

CREATE TABLE worktimes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    team_id INT NOT NULL,
    start_time INT NOT NULL,
    end_time INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (team_id) REFERENCES teams(id)
);

INSERT INTO teams (teamname, url_token) VALUES
('A', 'k3JH0q'),
('B', 'rSqElH'),
('C', 'Teh9Nb'),
('D', 'iDar79'),
('E', 'taNGUC'),
('F', 'mKPFwO'),
('G', 'qTCndG'),
('H', 'hhZjDt'),
('I', 'XLsTEJ'),
('J', 'fhvvIM'),
('K', 'qjVbn8'),
('L', 'g1rZzJ'),
('M', 'vi82cP'),
('N', 'rrDJCG'),
('O', '7xLL6t'),
('P', 'HWMXVm'),
('Q', 'gwraMB'),
('R', '9seg9w'),
('S', 'ykc5Kh'),
('T', 'V0VgIF'),
('U', 'E3gc2a'),
('V', 'Xzi9bc'),
('W', 'aVZcMH'),
('X', '6sIGu3'),
('Y', 'VE5Jcg'),
('Z', 'nNl09C');


-- テスト用のダミーデータ

-- password_hash は 'password' の ハッシュ値（SHA256）
INSERT INTO users (id, username, password_hash, team_id, created_at) VALUES 
(1, 'test', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8', 1, '2017-05-05 00:00:00.000+0000');


INSERT INTO channels (id, channel_name, channel_description, team_id, created_by, created_at) VALUES
(1, 'テストチャンネル', 'テスト用のチャンネルです', 1, '2017-05-05 00:00:00.000+0000');

INSERT INTO messages (id, content, user_id, channel_id, team_id, created_at) VALUES
(1, 'テストです', 1, 1, 1, '2017-05-05 00:00:00.000+0000');

INSERT INTO worktimes (id, user_id, team_id, start_time, end_time, created_at, updated_at) VALUES
(1, 1, 1, '2017-05-05 00:00:00', '2017-05-05 11:00:00', '2017-05-05 00:00:00.000+0000','2017-05-05 00:00:00.000+0000');