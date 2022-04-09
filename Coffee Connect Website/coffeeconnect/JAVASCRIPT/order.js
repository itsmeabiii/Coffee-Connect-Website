
document.getElementById('button1').addEventListener("click", function() {
	document.querySelector('.bg-modal').style.display = "flex";
});

document.querySelector('.close_but').addEventListener("click", function() {
	document.querySelector('.bg-modal').style.display = "none";
});

