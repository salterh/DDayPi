const express = require("express");
const rpio = require("rpio");
const app = express();
app.listen(3000, "localhost");
app.use(express.static("public"));

app.get("/gpio", (req, res) => {
    res.send({
        data: "justsomedata"
    });
})