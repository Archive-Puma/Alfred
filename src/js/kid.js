var font;
var Nodes;
var lastClick;
var SelectedNode;

function preload()
{
    font = loadFont('assets/fonts/OpenSans-SemiBold.ttf');
}

function setup()
{
    let canvas = createCanvas(windowWidth,windowHeight);
    canvas.parent('container');

    textSize(12);
    textFont(font);
    rectMode(CENTER);
    textAlign(CENTER);
    ellipseMode(CENTER);

    Nodes = [];
    lastClick = createVector(-1,-1);
}

function draw()
{
    background(color(46, 42, 35));

    for(var node of Nodes)
    {
        node.draw();
    }
}

function windowResized()
{
    resizeCanvas(windowWidth, windowHeight);
}

