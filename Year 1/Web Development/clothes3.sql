DROP TABLE IF EXISTS clothes;

CREATE TABLE clothes
(
    item_id INT AUTO_INCREMENT,
    category VARCHAR(30),
    quantity INT,
    price DECIMAL(5,2),
    img_url VARCHAR(60),
    img_alt VARCHAR(60),
    description TEXT,
    PRIMARY KEY (item_id)
);