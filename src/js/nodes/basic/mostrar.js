function Mostrar() {
    this.size = [60, 20];
    this.value = "";
    this.addInput("Texto", "", { label: "" });
}

Mostrar.title = "Mostrar";
Mostrar.desc = "Muestra el valor de la entrada";

Mostrar.prototype.onExecute = function() {
    if (this.inputs[0]) { this.value = this.getInputData(0); }
}

Mostrar.prototype.getTitle = function() {
    if (this.flags.collapsed) { return this.inputs[0].label; }
    return this.title;
}

Mostrar.toString = function(o) {
    if (o == null) {
        return "- -";
    } else if (o.constructor === Number) {
        return o.toFixed(6);
    } else if (o.constructor === Boolean)
    {
        return o ? "Verdadero" : "Falso";
    } else if (o.constructor === Array) {
        var str = "[";
        for (var i = 0; i < o.length; ++i) {
            str += Mostrar.toString(o[i]) + (i + 1 != o.length ? "," : "");
        }
        str += "]";
        return str;
    } else if (o.constructor === Object)
    {
        var json = JSON.stringify(o);
        if (json.length > 100)
        {
            console.log(o);
            json = "<JSON>";
        }
        return json;
    } else {
        return String(o);
    }
}

Mostrar.prototype.onDrawBackground = function(ctx) {
    this.inputs[0].label = Mostrar.toString(this.value);
}

LiteGraph.registerNodeType("Básico/Mostrar", Mostrar);