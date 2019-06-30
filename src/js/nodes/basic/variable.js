function Variable()
{
    this.addInput("", LiteGraph.ACTION);
    this.addInput("Nombre", "");
    this.addInput("Valor", 0);

    this.addOutput("", LiteGraph.EVENT);
    this.addOutput("Valor", 0);
}

Variable.title = "Variable";
Variable.desc = "Asigna un nombre a un valor";

Variable.prototype.getTitle = function() {
    if(this.flags.collapsed) {
        let nombre = this.getInputData(1);
        return nombre ? nombre : "< Variable >"; }
    return this.title;
}

Variable.prototype.onAction = function()
{
    let input_nombre = this.getInputData(1);
    let input_value = this.getInputData(2);

    if(input_nombre && input_value !== undefined) {
        variables_table[input_nombre] = input_value; }
    if(input_nombre && variables_table[input_nombre] !== undefined) {
        this.setOutputData(1, variables_table[input_nombre]);
        this.triggerSlot(0, "variable");
    }
}

LiteGraph.registerNodeType("Básico/Variable", Variable);