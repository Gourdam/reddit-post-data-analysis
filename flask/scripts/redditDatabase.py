import psycopg2
import psycopg2.extras

# SQL statement for posts_updates
sqlUpdatePost = """
INSERT INTO posts_updates(post_id, score, ratio, num_comments, timestamp_update)
    VALUES(
        %s,
        %s,
        %s,
        %s,
        %s
    );
"""

# SQL statement for posts
sqlNewPost = """
INSERT INTO posts(post_id, link, subreddit, title, author, active, timestamp_created)
    VALUES(
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s
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
    post_id = %s
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
    post_id = %s;
"""

sqlgetPostState = """
SELECT
    active
FROM
    posts
WHERE
    post_id = %s;
"""

sqlDeactivatePost = """
UPDATE
    posts
SET
    active = 0
WHERE
    post_id = %s;
"""
#converts the tuples(from the database) into a dictionary for ease of access
def dict_factory(cursor, row):
    d = {}
    for idx,col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

# REFACTOR CODE
class RedditDatabase:
    def __init__(self, database):
        self.database = database['database']
        self.user = database['user']
        self.password = database['password']
        self.host = database['host']

    def connectDB(self):
        return psycopg2.connect(database=self.database,
                                user=self.user,
                                password=self.password,
                                host=self.host)
#turns newData from redditBot into a tuple to store in database posts table
    def newPostTuple(self, newData):
        post_id = newData['post_id']
        link = newData['link']
        subreddit = newData['subreddit']
        title = newData['title']
        author = newData['author']
        active = newData['active']
        timestamp_created = newData['timestamp_created']
        return (post_id, link, subreddit, title, author, active, timestamp_created)
#turns updateData from redditBot into a tuple to store in database postsUpdates table
    def updatePostTuple(self, updateData):
        post_id = updateData['post_id']
        score = updateData['score']
        ratio = updateData['ratio']
        num_comments = updateData['num_comments']
        timestamp_update = updateData['timestamp_update']
        return (post_id, score, ratio, num_comments, timestamp_update)

#arguments is a generic parameter that takes in the tuples, this function allows us to commit anything to the database
    def updateDatabase(self, sqlStatement, arguments):
        database = self.connectDB()
        cursor = database.cursor()
        cursor.execute(sqlStatement, arguments)
        database.commit()
        cursor.close()
        database.close()
#updates the database with a new post
    def newPost(self, newData):
        arguments = self.newPostTuple(newData)
        self.updateDatabase(sqlNewPost, arguments)
#updates the database with a new post update
    def updatePost(self, updateData):
        arguments = self.updatePostTuple(updateData) #this is the parameter in the updateDatabase function
        self.updateDatabase(sqlUpdatePost, arguments)
        # Pulling all points when only 3 are needed. Must add an sql argument
        points = self.getPoints(updateData['post_id']) #updateData is the dictionary from the redditBot class
        if self.isSameValues(points):
            print("Post %s is stale!" % updateData['post_id']) #testing
            self.deactivatePost(updateData['post_id'])


    # getting values from database
#get the individual post from the database
    def getPost(self, post_id):
        connection = self.connectDB()
        c = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        c.execute(sqlGetPost, (post_id,))
        data = c.fetchone()
        c.close()
        return data
#get the points from the database
    def getPoints(self, post_id):
        connection = self.connectDB()
        c = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        c.execute(sqlGetPoints, (post_id,))
        data = c.fetchall() #fetches all the rows, iterate through the rows
        c.close()
        points = {
            'score': [],
            'ratio': [],
            'num_comments': [],
            'timestamp_update': []
        }
        #iterates through the rows to add to the points dictionary
        for row in data:
            points['score'].append(row['score'])
            points['ratio'].append(row['ratio'])
            points['num_comments'].append(row['num_comments'])
            points['timestamp_update'].append(row['timestamp_update'])
        return points

#all only evaluates true if all 3 comparisons are true
    def allSame(self, items):
        return all(x==items[0] for x in items) #compares all the terms in the array with x to see if same

    # count is >= 2 since score keeps changing from reddit algorithm
    def isSameValues(self, points):
        if len(points['score']) >= 3:
            count = 0
            for key, values in points.items():
                if key != 'timestamp_update': #only checks first three keys (points, num comments, ratio)
                    same_data = values[-3:] #takes last three points in array
                    if self.allSame(same_data):
                        count += 1
            if count >= 2:
                return 1
        return 0

    def isActivePost(self, post_id):
        connection = self.connectDB()
        c = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        c.execute(sqlgetPostState, (post_id,))
        data = c.fetchone()
        c.close()
        return data['active']

    def deactivatePost(self, post_id):
        self.updateDatabase(sqlDeactivatePost, (post_id,))
        print("Deactivating post %s" % post_id) #testing
