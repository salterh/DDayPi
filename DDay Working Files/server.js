const express = require("express");
const app = express();

app.listen(3000, "localhost");
app.use(express.static("public"));