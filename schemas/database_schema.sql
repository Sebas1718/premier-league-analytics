-- SQL Schema for Premier League Data

-- Table for Teams
CREATE TABLE teams (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    founded YEAR,
    home_ground VARCHAR(100),
    manager VARCHAR(100)
);

-- Table for Players
CREATE TABLE players (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    age INT,
    position VARCHAR(50),
    team_id INT,
    FOREIGN KEY (team_id) REFERENCES teams(id)
);

-- Table for Matches
CREATE TABLE matches (
    id INT PRIMARY KEY AUTO_INCREMENT,
    date DATETIME NOT NULL,
    home_team_id INT,
    away_team_id INT,
    home_team_score INT,
    away_team_score INT,
    FOREIGN KEY (home_team_id) REFERENCES teams(id),
    FOREIGN KEY (away_team_id) REFERENCES teams(id)
);

-- Table for Season Statistics
CREATE TABLE season_statistics (
    id INT PRIMARY KEY AUTO_INCREMENT,
    season VARCHAR(20) NOT NULL,
    team_id INT,
    matches_played INT,
    wins INT,
    draws INT,
    losses INT,
    FOREIGN KEY (team_id) REFERENCES teams(id)
);