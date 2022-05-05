const express = require("express");
const app = express();

app.listen(3000, "localhost");
app.use(express.static("public"));

app.get("/:one/:complete", handleRequest);

function handleRequest(req, res) {
    res.send({
        puzzle: Object.keys(req.params)[0],
        status: Object.keys(req.params)[1]
    });
}