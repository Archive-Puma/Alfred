LiteGraph.debug = false;

var graphcanvas = document.createElement("canvas");
graphcanvas.setAttribute("id", "graphcanvas");
document.body.append(graphcanvas);

var graph = new LGraph();
var canvas = new LGraphCanvas("#graphcanvas", graph);    
canvas.resize(1920,1080);

graph.start();
var variables_table = {};