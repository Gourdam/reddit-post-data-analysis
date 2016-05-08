import praw
import datetime
import calendar
import json
# check out multiprocessing module

r = praw.Reddit(user_agent="Pulls post data information in" +
                           " intervals and stores it")
# temp database
cache = []

def getTime():
    date = datetime.datetime.utcnow()
    utc_time = calendar.timegm(date.utctimetuple())
    return utc_time

def convertToJson(file):
    continue

class RedditBot:
    def __init__(self, uniqueID):
        self.uniqueID = uniqueID
        self.update_timestamp = getTime()
        self.recent_data = None

        update = r.get_submission(submission_id=self.uniqueID)
        self.link = self.update.permalink
        self.title = self.update.title
        self.author = self.update.author.name
        self.timestamp_created = self.post.created_utc
        # push data to the database

    def isStalePost(self, new_data):
        # change some_number later
        current_timestamp = getTime()
        if self.update_timestamp + some_number <= current_timestamp and
            self.recent_data == new_data:
            return True
        else:
            return False

    def pullDataManual(self, interval, num_iterations):
        for x in range(num_iterations):
            print("Updating post...")
            update = r.get_submission(submission_id=self.uniqueID)
            new_data = {
                'score': self.post.score,
                'ratio': self.post.upvote_ratio,
                'num_comments': self.post.num_comments
            }
            # send new_data to database but for not to local cache
            print("Caching...")
            cache.append(new_data)
            print("Success!")
            self.recent_data = new_data
            print("Sleeping for %d..." % interval)
            time.sleep(interval)

    def pullDataAuto(self):
        print("Updating post...")
        update = r.get_submission(submission_id=self.uniqueID)
        new_data = {
            'score': self.post.score,
            'ratio': self.post.upvote_ratio,
            'num_comments': self.post.num_comments
        }
        # send new_data to database
        if isStalePost(new_data):
            print("Post is stale! Exiting loop...")
            break
        self.recent_data = new_data