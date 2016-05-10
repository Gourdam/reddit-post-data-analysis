CREATE TABLE posts (
	post_id VARCHAR(6),
	link VARCHAR(512),
	subreddit VARCHAR (30),
	title VARCHAR(300),
	author VARCHAR(30),
	active BOOLEAN,
	timestamp_created INTEGER(12)
);