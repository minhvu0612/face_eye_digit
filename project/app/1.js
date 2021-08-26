

function FAER(argument) {
	// body...
	var x = document.getElementById("Face");
	var y = document.getElementById("Eye");
	var x1;
	var y1;
	
	eel.getFace_Eye()(function (array){
		x.innerHTML = array[0];
		y.innerHTML = array[1];
	});
}

function OJ(argument) {
	// body...
	var img = document.createElement("img");
	var select = document.getElementById("selection");
	var p = document.createElement("p");

	//var e = select.options[select.selectedIndex].text;
	img.src = "data_img/" + select.value;
	img.id  = "imgIn";
	p.innerHTML = "Predict: ";
	p.id = "pIn";
	var div = document.getElementById("div3");
	div.appendChild(p);
	div.appendChild(img);

	var set = document.getElementById("set");
	set.onclick = function(){RS();};
	set.innerHTML = "Reset";
}

function RS(argument){
	var img = document.getElementById("imgIn");
	var p   = document.getElementById("pIn");
	var div = document.getElementById("div3");
	div.removeChild(img);
	div.removeChild(p);
	
	var set = document.getElementById("set");
	set.onclick = function(){OJ();};
	set.innerHTML = "Set";
}

async function HDR(argument) {
	// body...
	var select = document.getElementById("selection");
	//console.log(typeof select.value);
	let value = await eel.prediction(select.value)();
	var p = document.getElementById("pIn");
	p.innerHTML = "Predict: " + value;
}