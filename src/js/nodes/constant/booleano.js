function Booleano() {
    this.addOutput("", false);
    this.size = [133, 48];
    this.widget = this.addWidget(
        "toggle",
        "Valor",
        null,
        this.setValue.bind(this)
    );
    this.widgets_up = true;
    this.addProperty("valor", false);
}

Booleano.title = "Booleano";
Booleano.desc = "Crea un texto";

Booleano.prototype.onExecute = function() {
    this.setOutputData(0, this.properties["valor"]);
}

Booleano.prototype.getTitle = function() {
    if (this.flags.collapsed) {
        return this.properties["valor"] ? "Verdadero" : "Falso"; }
    return this.title;
}

Booleano.prototype.onPropertyChanged = function(name, value) {
    this.widget.value = value;
}

Booleano.prototype.setValue = function(v) {
    this.properties["valor"] = v;
}

LiteGraph.registerNodeType("Constante/Booleano", Booleano);