import praw

class RedditBot:
    def __init__(self, unique_id):
        self.cache = []
        self.r = praw.Reddit(user_agent = "Pulls post data information in" +
                                            " intervals and stores it")
        self.post = self.r.get_submission(submission_id = unique_id)

    def record_submission(self):
        print("Updating...")
        update = {
            'link': self.post.permalink,
            'score': self.post.score,
        }