-- creates a new table 'unique_id'
-- description unique 'id=INT witht value 1', 'name=VARCHAR(256)'
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256) NOT NULL
);