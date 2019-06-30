function Alfred() {
    this.size = [164, 84];
    this.clicked = false;
    this._fontsize = 30;
    this._texts = [ "Empezar", "Resetear" ];
    this.button_text = this._texts[0];

    this.addProperty("corriendo", false);
    this.addProperty("programa", "");
}

Alfred.title = "Alfred";
Alfred.desc = "Inicia y restaura el programa";
Alfred.font = "Arial";

Alfred.prototype.onDrawForeground = function(ctx) {
    if (this.flags.collapsed) {
        return;
    }
    var margin = 10;
    ctx.fillStyle = "black";
    ctx.fillRect(
        margin + 1,
        margin + 1,
        this.size[0] - margin * 2,
        this.size[1] - margin * 2
    );
    ctx.fillStyle = "#AAF";
    ctx.fillRect(
        margin - 1,
        margin - 1,
        this.size[0] - margin * 2,
        this.size[1] - margin * 2
    );
    ctx.fillStyle = "#668";
    ctx.fillRect(
        margin,
        margin,
        this.size[0] - margin * 2,
        this.size[1] - margin * 2
    );

    if (this.button_text || this.button_text === 0) {
        var font_size = this._fontsize || 30;
        ctx.fillStyle = "white";
        ctx.textAlign = "center";
        ctx.font = font_size + "px " + Alfred.font;
        ctx.fillText(
            this.button_text,
            this.size[0] * 0.5,
            this.size[1] * 0.5 + font_size * 0.3
        );
        ctx.textAlign = "left";
    }
};

Alfred.prototype.onMouseDown = function(e, local_pos) {
    if (
        local_pos[0] > 1 &&
        local_pos[1] > 1 &&
        local_pos[0] < this.size[0] - 2 &&
        local_pos[1] < this.size[1] - 2
    ) {
        if(this.clicked)
        {
            graph.stop();
            graph.configure(JSON.parse(this.properties["programa"]));
            this.properties["programa"] = "";
            this.properties["corriendo"] = false;
            this.button_text = this._texts[0];
        } else {
            this.properties["programa"] = JSON.stringify(graph.serialize());
            this.properties["corriendo"] = true;
            graph.start();
            this.button_text = this._texts[1];
        }
        this.clicked = !this.clicked;
    }
};

LiteGraph.registerNodeType("Básico/Alfred", Alfred);