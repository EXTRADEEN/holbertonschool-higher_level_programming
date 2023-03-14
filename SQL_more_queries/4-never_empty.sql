-- creates a new table 'id_not_null'
-- description 'id=INT witht value 1', 'name=VARCHAR(256)'
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256) NOT NULL
);