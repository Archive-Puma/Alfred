import { createGzip } from "zlib";

let canvas = getElementById('canvas');
var ctx = canvas.getContext('2d');

ctx.moveTo(0,0);
ctx.lineTo(canvas.width, canvas.height);
ctx.stroke();