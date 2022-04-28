httpGetAsync("localhost:3000/puzzleone/complete");

function httpGetAsync(theUrl, callback) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function () {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
            //Callback goes here
        }
        xmlHttp.open("GET", theUrl, true); // true for asynchronous 
        xmlHttp.send();
        xmlHttp.onload = function () {
            console.log(xmlHttp.response);
        }
    }
}