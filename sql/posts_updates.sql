CREATE TABLE posts_updates (
	update_id INT IDENTITY(1, 1) NOT NULL
	post_id VARCHAR(6),
	score INTEGER(6),
	ratio DECIMAL(3, 2),
	num_comments INTEGER(10),
	timestamp_update INTEGER(11)
);
	