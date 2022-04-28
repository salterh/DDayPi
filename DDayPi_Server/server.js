const express = require("express");
const { redirect } = require("express/lib/response");
const app = express();

app.listen(3000, "localhost");
app.use(express.static("public"));

app.get('/puzzleone/:complete', puzzleOne);
app.get('/puzzleone/:reset', puzzleOne);

function puzzleOne(req, res) {
    var message;
    switch(Object.keys(req.params)[0]) {
        case "complete":
            message = {
                address: "/puzzlecomplete",
                info: "add"
            }
        break;
        case "reset":
            message = {
                address: "/reset",
                info: "reset"
            }
        break;
    }
    res.send(message);
}