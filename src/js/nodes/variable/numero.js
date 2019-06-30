function Numero() {
    this.addOutput("", "");
    this.size = [90, 60];
    this.properties = { valor: 1, pasos: 1 };

    this._remainder         = 0;
    this._precision         = 0;
    this._old_y             = -1;
    this._mouse_captured    = false;
}

Numero.title = "Número";
Numero.desc = "Genera un número constante";

Numero.pixels_threshold = 10;
Numero.markers_color = "#666";

Numero.prototype.onExecute = function() {
    this.setOutputData(0, this.properties["valor"]);
};

Numero.prototype.getTitle = function() {
    if (this.flags.collapsed) { return this.properties["valor"].toFixed(this._precision); }
    return this.title;
}

Numero.prototype.onDrawForeground = function(ctx) {
    if(this.flags.collapsed) { return; }

    var x = this.size[0] * 0.5;
    var h = this.size[1];
    if (h > 30) {
        ctx.fillStyle = Numero.markers_color;
        ctx.beginPath();
        ctx.moveTo(x, h * 0.1);
        ctx.lineTo(x + h * 0.1, h * 0.2);
        ctx.lineTo(x + h * -0.1, h * 0.2);
        ctx.fill();
        ctx.beginPath();
        ctx.moveTo(x, h * 0.9);
        ctx.lineTo(x + h * 0.1, h * 0.8);
        ctx.lineTo(x + h * -0.1, h * 0.8);
        ctx.fill();
        ctx.font = (h * 0.6).toFixed(1) + "px Arial";
    } else {
        ctx.font = (h * 0.6).toFixed(1) + "px Arial";
    }

    ctx.textAlign = "center";
    ctx.font = (h * 0.5).toFixed(1) + "px Arial";
    ctx.fillStyle = "#EEE";
    ctx.fillText(
        this.properties["valor"].toFixed(this._precision),
        x,
        h * 0.68
    );
};

Numero.prototype.onPropertyChanged = function(name, value) {
    var t = (this.properties["pasos"] + "").split(".");
    this._precision = t.length > 1 ? t[1].length : 0;
};

Numero.prototype.onMouseDown = function(e, pos) {
    if (pos[1] < 0) { return; }

    this._old_y = e.canvasY;
    this.captureInput(true);
    this._mouse_captured = true;

    return true;
};

Numero.prototype.onMouseMove = function(e) {
    if (!this._mouse_captured) { return; }

    var delta = this._old_y - e.canvasY;
    if (e.shiftKey) { delta *= 10; }
    if (e.metaKey || e.altKey) { delta *= 0.1; }
    this._old_y = e.canvasY;

    var steps = this._remainder + delta / Numero.pixels_threshold;
    this._remainder = steps % 1;
    steps = steps | 0;

    var v = Math.clamp(
        this.properties["valor"] + steps * this.properties["pasos"],
        Number.MIN_SAFE_INTEGER,
        Number.MAX_SAFE_INTEGER
    );
    this.properties["valor"] = v;
    this.graph._version++;
    this.setDirtyCanvas(true);
};

Numero.prototype.onMouseUp = function(e, pos) {
    if (e.click_time < 200) {
        var steps = pos[1] > this.size[1] * 0.5 ? -1 : 1;
        this.properties["valor"] = Math.clamp(
            this.properties["valor"] + steps * this.properties["pasos"],
            Number.MIN_SAFE_INTEGER,
            Number.MAX_SAFE_INTEGER
        );
        this.graph._version++;
        this.setDirtyCanvas(true);
    }

    if (this._mouse_captured) {
        this._mouse_captured = false;
        this.captureInput(false);
    }
};

LiteGraph.registerNodeType("Variable/Número", Numero);