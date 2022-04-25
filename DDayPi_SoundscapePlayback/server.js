const express = require("express");
const OSC = require("osc-js")
const app = express();

app.listen(3000, "localhost");
app.use(express.static("public"));

// const config = { udpClient: { port: 3001 } };
// const osc = new OSC({ plugin: new OSC.BridgePlugin(config) });
// osc.open({host: "127.0.0.1", port: 3001});