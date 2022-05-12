const express = require("express");
const app = express();

app.listen(3000, "localhost");
app.use(function(req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
  });
app.use(express.static("public"));

app.get("/:puzzleone", puzzleOne);

function puzzleOne(req, res) {
    res.send("hello");
}