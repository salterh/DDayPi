autowatch = 1;
inlets = 1;
outlets = 1;

var numbers = [];
var answer = [2,2,0,9,1,9,7,7];

function msg_float(args) {
    	numbers.push(args);
    	if (numbers.length > 8) {
		clear();
		numbers.push(args)
	}
	if (JSON.stringify(numbers) == JSON.stringify(answer)) {
		outlet(0, "bang");
		clear();
	}
}

function clear() {
	numbers = [];
}
