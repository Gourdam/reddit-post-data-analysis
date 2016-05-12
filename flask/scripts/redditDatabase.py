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
INSERT INTO posts(post_id, link, subreddit, title, author, active, timestamp_created)
    VALUES(
        ?,
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
    post_id = ?
ORDER BY
    timestamp_update;
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

sqlgetPostState = """
SELECT
    active
FROM
    posts
WHERE 
    post_id = ?;
"""

sqlDeactivatePost = """
UPDATE
    posts
SET
    active = 0
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
        active = newData['active']
        timestamp_created = newData['timestamp_created']
        return (post_id, link, subreddit, title, author, active, timestamp_created)

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
        points = {
            'score': [],
            'ratio': [],
            'num_comments': [],
            'timestamp_update': []
        }
        for row in data:
            points['score'].append(row['score'])
            points['ratio'].append(row['ratio'])
            points['num_comments'].append(row['num_comments'])
            points['timestamp_update'].append(row['timestamp_update'])
        if self.isSameValues(points):
            self.deactivatePost(post_id)
        return points

    def allSame(self, items):
        return all(x==items[0] for x in items)

    def isSameValues(self, points):
        if len(points['score']) >= 3:
            for key, values in points.items():
                if key != 'timestamp_update':
                        if self.allSame(values):
                            return 1
            return 0

    def isActivePost(self, post_id):
        connection = self.connectDB()
        connection.row_factory = dict_factory
        c = connection.cursor()
        c.execute(sqlgetPostState, (post_id,))
        data = c.fetchone()
        c.close()
        return data['active']

    def deactivatePost(self, post_id):
        self.updateDatabase(sqlDeactivatePost, (post_id,))
