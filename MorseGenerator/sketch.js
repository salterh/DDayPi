var timeout;
var code = ". . .   . -   - .   - . .   - - .   . -   -   .";
var charCounter = 0;
var toggle;
var osc;

function setup() {
  createCanvas(400, 400);
  background(255);
  toggle = createCheckbox("Toggle Morse", false);
  toggle.position(10, 10);
  toggle.changed(startEvent);
  osc = new p5.Oscillator('sine');
  osc.freq(440);
  osc.amp(0);
  osc.start();
}

function startEvent() {
  if (toggle.checked()) {
    timeout = setTimeout(output, 0);
  } else {
    clearTimeout(timeout);
    charCounter = 0;
  }
}

function output() {
  background(255);
  var size = 0;
  var time = 0;
  switch (code[charCounter]) {
    case ".":
      time = 500;
      size = 100;
      osc.amp(0.4, 0.2);
      break;
    case "-":
      time = 1500;
      size = 100;
      osc.amp(0.4, 0.2);
      break;
    case " ":
      time = 500;
      size = 0;
      osc.amp(0, 0.2);
      break;
    case "   ":
      time = 1500;
      size = 0;
      osc.amp(0, 0.2);
      break;
    case "/":
      time = 3500;
      size = 0;
      osc.amp(0, 0.2);
      break;
  }
  console.log(osc);
  charCounter++;
  if (charCounter <= code.length) timeout = setTimeout(output, time);
  else {
    size = 0;
    charCounter = 0;
    timeout = setTimeout(output, 7000);
    osc.amp(0, 0.2);
    console.log("Finished");
  }
  fill(50);
  ellipse(width / 2, height / 2, size);
}
