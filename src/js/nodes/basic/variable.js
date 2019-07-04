function Variable()
{
    this.nombre_widget = this.addWidget(
        "text",
        "Nombre",
        "",
        function() {}
    );

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
        var nombre = this.getInputData(1);
        return nombre ? nombre : "< Variable >"; }
    return this.title;
}

Variable.prototype.onAction = function()
{
    var input_nombre = this.getInputData(1);
    var input_value = this.getInputData(2);

    if(input_nombre !== undefined && input_nombre.constructor === String) {
        this.nombre_widget.value = input_nombre; }
    var nombre = this.nombre_widget.value;
    if(nombre === undefined || nombre.constructor !== String || nombre === "") {
        return; }
    if(input_value !== undefined) {
        variables_table[nombre] = input_value; }
    if(variables_table[nombre] !== undefined) {
        this.setOutputData(1, variables_table[nombre]);
        this.triggerSlot(0, "variable");
    }
}

LiteGraph.registerNodeType("Básico/Variable", Variable);