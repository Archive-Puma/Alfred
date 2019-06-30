function Texto() {
    this.addOutput("", "");
    this.size = [100, 30];
    this.widget = this.addWidget(
        "text",
        "",
        "",
        this.setValue.bind(this)
    );
    this.widgets_up = true;
    this.addProperty("texto", "")
}

Texto.title = "Texto";
Texto.desc = "Crea un texto";

Texto.prototype.onExecute = function() {
    this.setOutputData(0, this.properties["texto"]);
};

Texto.prototype.getTitle = function() {
    if (this.flags.collapsed) { return this.properties["texto"]; }
    return this.title;
};

Texto.prototype.onPropertyChanged = function(name, value) {
    this.widget.value = value;
};

Texto.prototype.setValue = function(v) {
    this.properties["texto"] = v;
};

LiteGraph.registerNodeType("Variable/Texto", Texto);