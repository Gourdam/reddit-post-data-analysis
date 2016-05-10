CREATE TABLE posts_updates (
	post_id VARCHAR(6),
	score INTEGER(6),
	ratio DECIMAL(3, 2),
	num_comments INTEGER(10),
	is_stale BOOLEAN,
	timestamp_update INTEGER(11)
);
	