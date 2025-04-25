-- （開発時のみの実装）すでに存在する場合は削除
DROP DAtABASE chatapp;
DROP USER 'testuser';

CREATE USER 'testuser' IDENTIFIED BY 'testuser';
CREATE DATABASE chatapp;
USE chatapp
GRANT ALL PRICILEGES ON chatapp.* TO 'testuser';

CREATE TABLE teams (
    id INT AUTO_INCReMENT PRIMARY KEY,
    teamname VARCHAR(50) UNIQUE NOT NULL,
    url_token VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    team_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    FOREIGN KEY (team_id) PREFERENCES teams(id),
);

CREATE TABLE channels (
    id INT AUTO_INCREMENT PRIMARY KEY,
    channel_name VARCHAR(100) NOT NULL,
    channel_description TEXT, NULL,
    created_by INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (created_by) REFERENCES users(id),
);

CREATE TABLE channel_members (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    channel_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (channel_id) REFERENCES channels(id)
);

CREATE TABLE message (
    id INT AUTO_INCREMENT PRIMARY KEY,
    content TEXT NOT NULL,
    user_id INT NOT NULL,
    channel_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (channel_id) REFERENCES channels(id)
);

CREATE TABLE worktime (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    start_time_hour INT NOT NULL,
    start_time_minute INT NOT NULL,
    end_time_hour INT NOT NULL,
    end_time_minute INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
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


-- この後にテスト用のダミーデータを入れる必要がある（？）