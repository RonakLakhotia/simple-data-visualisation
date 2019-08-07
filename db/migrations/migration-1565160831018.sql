DROP TABLE IF EXISTS steps;

CREATE TABLE IF NOT EXISTS steps (
    id SERIAL PRIMARY KEY,
    participant_id VARCHAR(50) NOT NULL,
    week INTEGER,
    monday INTEGER,
    tuesday INTEGER,
    wednesday INTEGER,
    thursday INTEGER,
    friday INTEGER,
    saturday INTEGER,
    sunday INTEGER
);
