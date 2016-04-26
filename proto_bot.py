import praw
import pprint
import time


class RedditBot:
    def __init__(self, user_agent):
        self.cache = []
        self.r = praw.Reddit(user_agent = user_agent)
        # Hardcoded to test post right now
        self.post = self.r.get_submission(submission_id = "4ggj41")

    def login(self):
        self.r.login()

    def record_submission(self):
        print ("Updating...")
        update = {
            'link': self.post.permalink,
            'score': self.post.score,
            'upvote_ratio': self.post.upvote_ratio,
            'num_comments': self.post.num_comments
        }
        self.cache.append(update)
        print ("Cached! Sleeping for 5 seconds...")

    def output_submission(self):
        pprint.pprint(vars(self.post))
        print(self.post)

bot = RedditBot("test")
count = 0
while count <= 5:
    bot.record_submission()
    time.sleep(5)
    count += 1

pprint.pprint(bot.cache)
