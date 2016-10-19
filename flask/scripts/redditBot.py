import praw
#PRAW =  “Python Reddit API Wrapper”, python package that allows for access to reddit’s API.
import sqlite3

from . import utils

#creating praw object
r = praw.Reddit(user_agent="Pulls post data information in" +
                           " intervals and stores it")

class RedditBot:
    def __init__(self, postID):
        self.postID = postID
        self.updateTimestamp = utils.getTime() #deprecated
        self.recentData = None #deprecated

#returns an submission object with all the info
    def get_submission(self):
        return r.get_submission(submission_id=self.postID)

    def newPost(self):
        print("New post! %s" % (self.postID)) #testing
        post = self.get_submission()
        newData = {
            'post_id': self.postID,
            'link': post.permalink,
            'subreddit': post.subreddit.display_name,
            'title': post.title,
            'author': post.author.name,
            'active': True,
            'timestamp_created': int(post.created_utc)
        }
        return newData

    def updateData(self):
        print("Updating post %s..." % (self.postID)) #testing
        update =self.get_submission()
        newData = {
            'post_id': self.postID,
            'score': update.score,
            'ratio': update.upvote_ratio,
            'num_comments': update.num_comments,
            'timestamp_update': utils.getTime()
        }
        print("Sending data for %s to database..." %(self.postID))
        return newData
