## Reddata - Reddit Post Data Analysis Web-app
#####by Jordan Hu and Shabab Ayub - http://reddata.herokuapp.com/

###Description
Reddata is a web-app that allows a user to visualize the data related to a Reddit post. Scroll down to check out pictures!

##Background:
The web-app **parses a given Reddit post URL**. Using a bot made with **Python**, the server continuously updates information regarding the specified requests to the Reddit API which is stored in a **SQL database**. Then, a **JavaScript charting library, Chart.JS**, is used to **analyze and present the data** in a user-friendly manner. An added feature allows the program to intelligently decide to stop requesting after a post stagnates in activity. 

The purpose of this web-app is to present and analyze relevant data (upvote ratio, points, number of comments) on a Reddit post.  It would especially be **useful for smaller subreddits** such as a university subreddit, to pinpoint what style of posts the population resonates with. Reddata essentially allows a user to **get a glimpse into the psyche of the ever-active communities of Reddit!**

The reason we made Reddata was because we wanted experience with web-development and data analytics. 

###How to:
######Current Status: Refactoring to use PostgreSQL to deploy to Heroku, hence continue with following local implmentation.

Run ```python app.py``` in terminal to launch the web-app locally. Type ```localhost:5000``` into the browser to arrive at the home page of the web-app. Enter a Reddit post URL into the search bar (e.g.https://www.reddit.com/r/dataisbeautiful/comments/4iw59p/3point_attempts_over_time_in_the_nba_oc/). Refresh the page once the 3 graphs appear and continue to refresh in 5 minute intervals to see the data on the graphs updated. 

####Requirements to run:
The following list of items are required to run the ```app.py``` file. Use ```pip install``` to install them into a virtural environment (recommended). 

```
decorator==4.0.9
Flask==0.10.1
gunicorn==19.5.0
itsdangerous==0.24
Jinja2==2.8
MarkupSafe==0.23
praw==3.4.0
requests==2.10.0
six==1.10.0
update-checker==0.11
Werkzeug==0.11.9
```
####Example screenshots:
![alt tag](https://github.com/Gourdam/reddit-post-data-analysis/blob/master/pictures/reddata-index.png)
![alt tag](https://github.com/Gourdam/reddit-post-data-analysis/blob/master/pictures/reddata-stats.png)
![alt tag](https://github.com/Gourdam/reddit-post-data-analysis/blob/master/pictures/reddata-stats-updated.png)
![alt tag](https://github.com/Gourdam/reddit-post-data-analysis/blob/master/pictures/reddata-stats-updated2.png)

##Further Implementation: 
- Improve user experience
- Implement error handling
- Implement example usage
- Generate Python test scripts to optimally test every feature of the web-app
