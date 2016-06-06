import re
from datetime import datetime
import calendar

def getPostID(url):
    urlRegex = re.compile(r'/comments/(.*?)/')
    post_id = urlRegex.search(url)
    try:
    	return post_id.group(1)
    except:
    	return False

def getTime():
    date = datetime.utcnow()
    utc_time = calendar.timegm(date.utctimetuple())
    return utc_time