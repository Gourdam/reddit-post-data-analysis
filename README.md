## Reddata - Reddit Post Data Analysis Web-app
##### by Jordan Hu and Shabab Ayub - http://reddata.herokuapp.com/

### Description
Reddata is a web-app that allows a user to visualize the data related to a Reddit post. Scroll down to check out pictures!

## Background:
The web-app **parses a given Reddit post URL**. Using a bot made with **Python**, the server continuously updates information regarding the specified requests to the Reddit API which is stored in a **SQL database**. Then, a **JavaScript charting library, Chart.JS**, is used to **analyze and present the data** in a user-friendly manner. An added feature allows the program to intelligently decide to stop requesting after a post stagnates in activity. 

The purpose of this web-app is to present and analyze relevant data (upvote ratio, points, number of comments) on a Reddit post.  It would especially be **useful for smaller subreddits** such as a university subreddit, to pinpoint what style of posts the population resonates with. Reddata essentially allows a user to **get a glimpse into the psyche of the ever-active communities of Reddit!**

The reason we made Reddata was because we wanted experience with web-development and data analytics. 

#### Example screenshots :
![alt tag](https://github.com/Gourdam/reddit-post-data-analysis/blob/master/pictures/reddata-index.png)
![alt tag](https://github.com/Gourdam/reddit-post-data-analysis/blob/master/pictures/reddata-stats.png)
![alt tag](https://github.com/Gourdam/reddit-post-data-analysis/blob/master/pictures/reddata-stats-updated.png)
![alt tag](https://github.com/Gourdam/reddit-post-data-analysis/blob/master/pictures/reddata-stats-updated2.png)

## Further Implementation : 
- Improve user experience
- Implement error handling
- Test every feature of the web-app
