function Matematicas()
{
    this.op = this.addWidget(
        "combo",
        "",
        "+",
        function() {},
        { values: [ "+", "-", "*", "/", "^", "%"] }
    );
    this.addInput("", LiteGraph.ACTION);
    this.addInput("A", undefined);
    this.addInput("B", undefined);
    this.addOutput("", LiteGraph.EVENT);
    this.addOutput("=", 0);
}

Matematicas.title = "Matemáticas";
Matematicas.desc = "Realiza la operación aritmética sobre dos valores";

Matematicas.prototype.getTitle = function()
{
    if(this.flags.collapsed) { return this.op.value; }
    return this.title;
}

Matematicas.prototype.onAction = function()
{
    let A = this.getInputData(1);
    let B = this.getInputData(2);
    if(A !== undefined && B !== undefined &&
        A.constructor === Number && B.constructor === Number) {
        switch(this.op.value)
        {
            case "+": this.setOutputData(1, A + B); break;
            case "-": this.setOutputData(1, A - B); break;
            case "*": this.setOutputData(1, A * B); break;
            case "/": this.setOutputData(1, A / B); break;
            case "^": this.setOutputData(1, A ** B); break;
            case "%": this.setOutputData(1, A % B); break;
        }
        this.triggerSlot(0, "matematicas");
    } else { this.setOutputData(1, undefined); }
}

LiteGraph.registerNodeType("Operación/Matematicas", Matematicas);