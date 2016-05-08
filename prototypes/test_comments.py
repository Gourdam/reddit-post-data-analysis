import praw
import pprint

r = praw.Reddit(user_agent = "hey it's me")
post = r.get_submission(submission_id="4ggj41")
comments = post.comments
kevin = comments[0]

pprint.pprint(vars(kevin))
