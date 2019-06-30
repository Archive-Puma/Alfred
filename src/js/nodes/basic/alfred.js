function Alfred()
{
    this.addWidget(
        "button",
        "Empezar",
        null,
        this.start.bind(this)
    );

    this.addOutput("Inicio", LiteGraph.EVENT);
}

Alfred.title = "Alfred";
Alfred.desc = "Panel de control";

Alfred.prototype.start = function()
{
    this.triggerSlot(0, "inicio");
}

LiteGraph.registerNodeType("Básico/Alfred", Alfred);