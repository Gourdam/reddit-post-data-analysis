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
//passing in the dictionaries through the templates from app.py, they now become javascript objects through the double braces 
var information = {{information}};
var points = {{points}};

var poster = information[3];
var postURL = information[0];
var titles = information[2];
var sub = information[1];


if (titles.length > 22){
	titles = titles.substring(0,22) + " -...";
	console.log(titles);
}

var scores = points.score;
var comments = points.num_comments;
var times = points.timestamp_update;
var rat = points.ratio; 

var localtime = ["entry"];

//converts every timestamp in the times array to something humans can read
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
