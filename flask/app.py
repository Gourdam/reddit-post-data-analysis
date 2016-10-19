# Standard
from flask import Flask, render_template, redirect, url_for, request, session,\
    flash, g, jsonify
import re
import time

# labels: list
# data list
from multiprocessing import Process

# Private - utils is the regex, redditBot is the bot class, redditDatabase is the actually storing and extracting from database
from scripts import utils, redditBot, redditDatabase

# create application object
app = Flask(__name__)
# change database name later
app.database =  {
    'database': 'reddit_data',
    'user': 'reddit_data',
    'password': 'reddit_data',
    'host': 'localhost'
}
# secret key for cookies *MUST CHANGE FOR SECURITY*
app.secret_key = b'\xd0\x10\x0b$\x0fk\xbe%\xc6\x1b\xe4\xd1\xf0\xe0\xd4\x0210\xc5R\x80X\x98+'

# landing page with text field
# route() decorator to tell Flask what URL should trigger our function.
@app.route('/', methods=['GET', 'POST'])
def home():
    error = None
    if request.method == 'POST':
        session['url'] = request.form['url'] #storing this information while the user is browsing
        session['isBotOn'] = False #bot isn't on yet
        if (utils.getPostID(session['url']) == False):
            error = "You're tripping! Enter a reddit post URL!"
        else:
            return redirect(url_for('results'))
    return render_template('page.html', error=error)

# analysis page that displays post data
@app.route('/results')
def results():
    if not session['isBotOn']:
        session['postID'] = utils.getPostID(session['url'])
        bot = redditBot.RedditBot(session['postID'])
        newData = bot.newPost()
        with app.app_context(): #need to specify the context so flask can find the "application"
            g.db = redditDatabase.RedditDatabase(app.database)
            g.db.newPost(newData)
        p = Process(target=updatePost, args=(bot,)) #the argument bot is the redditBot object that grabs from the API
        p.start()
        session['isBotOn'] = True
    with app.app_context():
        g.db = redditDatabase.RedditDatabase(app.database)
        information = g.db.getPost(session['postID'])
        points = g.db.getPoints(session['postID'])
    return render_template('results.html', information=information, points=points)

def updatePost(bot):
    with app.app_context():
        g.db = redditDatabase.RedditDatabase(app.database)
        while True:
            if not g.db.isActivePost(bot.postID):
                break
            updateData = bot.updateData()
            g.db.updatePost(updateData)
            print("Post %s updated!" % bot.postID)
            # post pulls every 300 seconds
            time.sleep(60)
        print("Post %s not active!" % bot.postID)

# run app
if __name__ == "__main__":
    app.run(debug=True)
