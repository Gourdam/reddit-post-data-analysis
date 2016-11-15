function httpGet(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}



function convertTimestamp(timestamp) {
  var d = new Date(timestamp * 1000),	// Convert the passed timestamp to milliseconds
		yyyy = d.getFullYear(),
		mm = ('0' + (d.getMonth() + 1)).slice(-2),	// Months are zero based. Add leading 0.
		dd = ('0' + d.getDate()).slice(-2),			// Add leading 0.
		hh = d.getHours(),
		h = hh,
		min = ('0' + d.getMinutes()).slice(-2),		// Add leading 0.
		ampm = 'AM',
		time;
			
	if (hh > 12) {
		h = hh - 12;
		ampm = 'PM';
	} else if (hh === 12) {
		h = 12;
		ampm = 'PM';
	} else if (hh == 0) {
		h = 12;
	}
	
	// ie: 2013-02-18, 8:35 AM	
	time = h + ':' + min + ' ' + ampm;
		
	return time;
}
//var data = httpGet('/getpostupdate'); 
var information = {{information|safe}};
var points = {{points|safe}};

var poster = information.author;
var links = information.link;
var titles = information.title;
var sub = information.subreddit;

var scores = points.score;
var comments = points.num_comments;
var times = points.timestamp_update;
var rat = points.ratio; 

var localtime = ["entry", "entry2", "entry3"];

for (var i = 0; i < times.length; i++) {
	localtime[i] = convertTimestamp(times[i]);
}

console.log(poster);
console.log(links);
console.log(titles);
console.log(sub);

console.log(scores);
console.log(comments);
console.log(times);
console.log(rat);
console.log(localtime);
