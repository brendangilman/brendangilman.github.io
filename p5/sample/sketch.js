function setup() {
  // put setup code here
  createCanvas(480, 480);
  background(122, 132, 80)
}

function draw() {
  // put drawing code here
  if (mouseIsPressed) {
  fill(122, 132, 80);
  } else {
  fill(206,121,10);
  }
  ellipse(mouseX, mouseY, 80, 80);
  }
