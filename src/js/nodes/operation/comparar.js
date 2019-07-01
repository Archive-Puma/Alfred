function Comparar()
{
    this.addInput("", LiteGraph.ACTION);
    this.addInput("A", undefined);
    this.addInput("B", undefined);
    this.addOutput("", LiteGraph.EVENT);
    this.addOutput("Resultado", LiteGraph.EVENT);
}

Comparar.title = "Comparar";
Comparar.desc = "Compara dos valores y devuelve verdadero o falso";

Comparar.prototype.onAction = function()
{
    let A = this.getInputData(1);
    let B = this.getInputData(2);
    if(A !== undefined && B !== undefined) {
        this.setOutputData(1, A === B);
        this.triggerSlot(0, "comparar");
    } else { this.setOutputData(1, undefined); }
}

LiteGraph.registerNodeType("Operación/Comparar", Comparar);