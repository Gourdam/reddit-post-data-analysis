# Standard
from flask import Flask, render_template, redirect, url_for, request, session,\
    flash, g
import sqlite3
import re

# Private
from scripts import utils, redditbot

# create application object
app = Flask(__name__)
# change database name later
app.database = "proto_database.db"

# secret key for cookies *MUST CHANGE FOR SECURITY*
app.secret_key = b'\xd0\x10\x0b$\x0fk\xbe%\xc6\x1b\xe4\xd1\xf0\xe0\xd4\x0210\xc5R\x80X\x98+'

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

# SQL statement for posts
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

# landing page with text field
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        session['url'] = request.form['url']
        return redirect(url_for('analysis'))
    return render_template('index.html')

# analysis page that displays post data
@app.route('/analysis')
def analysis():
    postID = utils.getPostID(session['url'])
    bot = redditbot.RedditBot(postID)
    newData = bot.newPost()
    newPostDB(newData)
    return render_template('analysis.html')

def connectDB():
    return sqlite3.connect(app.database)

def newPostDB(newData):
    g.db = connectDB()

    post_id = newData['post_id']
    link = newData['link']
    subreddit = newData['subreddit']
    title = newData['title']
    author = newData['author']
    timestamp_created = newData['timestamp_created']
    g.db.execute(sqlNewPost, (post_id, link, subreddit, title, author, timestamp_created))

    g.db.commit()
    g.db.close()

def updatePostDB(updateData):

# run app
if __name__ == "__main__":
    app.run(debug=True)
