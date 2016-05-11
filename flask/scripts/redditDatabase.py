import sqlite3

# SQL statement for posts_updates
sqlUpdatePost = """
INSERT INTO posts_updates(post_id, score, ratio, num_comments, timestamp_update)
    VALUES(
        ?,
        ?,
        ?,
        ?,
        ?
    );
"""

# SQL statement for posts *MUST ADD active field later
sqlNewPost = """
INSERT INTO posts(post_id, link, subreddit, title, author, timestamp_created)
    VALUES(
        ?,
        ?,
        ?,
        ?,
        ?,
        ?
    );
"""

sqlGetPoints = """
SELECT
    score,
    ratio,
    num_comments,
    timestamp_update
FROM
    posts_updates
WHERE
    post_id = ?;
"""

sqlGetPost = """
SELECT
    link,
    subreddit,
    title,
    author
FROM
    posts
WHERE
    post_id = ?;
"""

def dict_factory(cursor, row):
    d = {}
    for idx,col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

# REFACTOR CODE
class RedditDatabase:
    def __init__(self, database):
        self.database = database

    def connectDB(self):
        return sqlite3.connect(self.database)

    def newPostTuple(self, newData):
        post_id = newData['post_id']
        link = newData['link']
        subreddit = newData['subreddit']
        title = newData['title']
        author = newData['author']
        timestamp_created = newData['timestamp_created']
        return (post_id, link, subreddit, title, author, timestamp_created)

    def updatePostTuple(self, updateData):
        post_id = updateData['post_id']
        score = updateData['score']
        ratio = updateData['ratio']
        num_comments = updateData['num_comments']
        timestamp_update = updateData['timestamp_update']
        return (post_id, score, ratio, num_comments, timestamp_update)

    def updateDatabase(self, sqlStatement, arguments):
        database = self.connectDB()
        database.execute(sqlStatement, arguments)
        database.commit()
        database.close()

    def newPost(self, newData):
        arguments = self.newPostTuple(newData)
        self.updateDatabase(sqlNewPost, arguments)

    def updatePost(self, updateData):
        arguments = self.updatePostTuple(updateData)
        self.updateDatabase(sqlUpdatePost, arguments)

    # getting values from database

    def getPost(self, post_id):
        connection = self.connectDB()
        connection.row_factory = dict_factory
        c = connection.cursor()
        c.execute(sqlGetPost, (post_id,))
        data = c.fetchone()
        c.close()
        return data

    def getPoints(self, post_id):
        connection = self.connectDB()
        connection.row_factory = dict_factory 
        c = connection.cursor()
        c.execute(sqlGetPoints, (post_id,))
        data = c.fetchall()
        c.close()
        return data

