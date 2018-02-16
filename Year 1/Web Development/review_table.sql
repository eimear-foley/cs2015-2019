DROP TABLE IF EXISTS review_table;

CREATE TABLE review_table
(
   review_id INT NOT NULL,
   username VARCHAR(255) NOT NULL,
   review TEXT NOT NULL,
   item_id INT NOT NULL,
   star INT NOT NULL,
   curr_time TIMESTAMP NOT NULL,
   helpful_count INT NOT NULL,
   PRIMARY KEY (review_id)
);

select * from review_table;

