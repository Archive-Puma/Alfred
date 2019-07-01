function Siempre()
{
    this.addOutput("", LiteGraph.EVENT);
}

Siempre.title = "Siempre";
Siempre.desc = "Genera un flujo constante";

Siempre.prototype.onExecute = function()
{
    this.triggerSlot(0, "siempre");
}

LiteGraph.registerNodeType("Control/Siempre", Siempre);