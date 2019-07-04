function Union()
{
    this.addInput("", LiteGraph.ACTION);
    this.addInput("", LiteGraph.ACTION);
    this.addOutput("", LiteGraph.EVENT);
}

Union.title = "Unión";
Union.desc = "Unión entre de dos flujos";

Union.prototype.onAction = function()
{
    this.triggerSlot(0, "union");
}

LiteGraph.registerNodeType("Control/Unión", Union);