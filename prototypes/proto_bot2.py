'''
data = {
    labels: ["Monday", "Tuesday", "Wednesday", "etc"]
    datasets: [
    {
        label: "The First Dataset",
        fillColor: "rgba(153,0,76,0.2)", // magenta
        strokeColor: "rgba(153,0,76,1)", // magenta
        pointColor: "rgba(153,0,76,1)", // magenta
        pointStrokeColor: "#fff", // white
        pointHighlightFill: "#fff", // white
        pointHighlightStroke: "rgba(153,0,76,1)", // magenta
        data: [100, 34, 21, 56, 23, 90, 40]
    }]
}
'''
import praw
import json
import time
import pprint

class RedditBot:
    def __init__(self, unique_id):
        self.cache = []
        self.r = praw.Reddit(user_agent = "Pulls post data information in" +
                                            " intervals and stores it")
        self.unique_id = unique_id

    def record_submission(self):
        print("Updating...")
        '''
        Relevant data:
        permalink, title, author, created, created_utc, score, upvote_ratio, num_comments, _comments, _has_fetched
        '''
        self.post = self.r.get_submission(submission_id = self.unique_id)
        update = {
            'link': self.post.permalink,
            'title': self.post.title,
            'author': self.post.author.name,
            'timestamp_created': int(self.post.created_utc),
            'score': int(self.post.score),
            'ratio': self.post.upvote_ratio,
            'num_comments': int(self.post.num_comments)
            #'comments': self.post._comments
        }
        self.cache.append(update)
        print("Cached!")
        print(json.dumps(update))

    def pull_data(self, interval, num_iterations):
        for x in range(num_iterations):
            self.record_submission()
            print("Sleeping for %d seconds..." % interval)
            time.sleep(interval)

class CommentBot:
    def __init__(self, comment):
        self.comment = comment

    def record_comment(self):
        print("Updating...")
        


bot = RedditBot("4ggj41")
bot.pull_data(5, 5)
pprint.pprint(bot.cache)    
