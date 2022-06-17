const express = require("express");
const fs = require('fs');

const app = express();
app.listen(3000, "localhost");
app.use(express.static("public"));

app.get("/startMic", (req, res) => {

    res.send({
        data: micInstance
    });
})