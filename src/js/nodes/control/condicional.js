function Condicional()
{
    this.addInput("", LiteGraph.ACTION);
    this.addInput("Valor", 0);
    this.addOutput("Verdadero", LiteGraph.EVENT);
    this.addOutput("Falso", LiteGraph.EVENT);
}

Condicional.title = "Condicional";
Condicional.desc = "Crear una intersección del flujo principal del programa";

Condicional.prototype.onAction = function()
{
    var condition = this.getInputData(1);
    if(condition === true) { this.triggerSlot(0, "condicional verdadero"); }
    else if(condition === false) { this.triggerSlot(1, "condicional falso"); }
}

LiteGraph.registerNodeType("Control/Condicional", Condicional);