const mongodb = require("mongojs");

function MongoDB() {
    this.size = [60, 20];
    this.uri_widget = this.addWidget(
        "text",
        "URI",
        "",
        this.setURI.bind(this)
    );
    this.collection_widget = this.addWidget(
        "text",
        "Colección",
        "",
        this.setCollection.bind(this)
    );
    this.document_widget = this.addWidget(
        "number",
        "Documento",
        0,
        this.setDocument.bind(this),
        { step: 1, precision: 0 }
    );

    this.addWidget(
        "button",
        "Obtener",
        null,
        this.connectSocket.bind(this)
    );

    this.addInput("", LiteGraph.ACTION);
    this.addOutput("", LiteGraph.EVENT);
    this.addOutput("json", []);

    this.properties = {
        URI: "localhost:27017/db",
        coleccion: "coleccion",
        documento: 0
    };

    this.db = null;
    this._error = false;
}

MongoDB.title = "MongoDB";
MongoDB.desc = "Conexión a una MongoDB";

MongoDB.prototype.connectSocket = function() {
    if (typeof mongodb == "undefined") {
        if (!this._error) {
            console.error("Mongojs no está instalado.");
        }
        this._error = true;
        return;
    }

    let that = this;
    this.db = mongodb(this.properties["URI"], [ this.properties["coleccion"] ]);
    this.db[this.properties["coleccion"]].find(function(err, docs)
    {
        let index = that.properties["documento"];
        if(err || index >= docs.length) { that.setOutputData(1, []); }
        else { that.setOutputData(1, docs[index]); }
    });

    if(this.outputs[0]) { this.triggerSlot(0, "mongodb"); }
};

MongoDB.prototype.onAction = function()
{
    this.connectSocket();
}

MongoDB.prototype.setURI = function(URI) {
    this.properties["URI"] = URI;
    this.uri_widget.value = URI;
};

MongoDB.prototype.setCollection = function(coleccion) {
    this.properties["coleccion"] = coleccion;
    this.collection_widget.value = coleccion;
};

MongoDB.prototype.setDocument = function(documento) {
    documento = Math.round(documento);
    this.properties["documento"] = documento;
    this.document_widget.value = documento;
};

MongoDB.prototype.onPropertyChanged = function(name, value) {
    if (name == "URI") { this.uri_widget.value = value; }
    else if (name == "coleccion") { this.collection_widget.value = value; }
    else if (name == "documento") { this.document_widget.value = Math.round(value); }
};

LiteGraph.registerNodeType("Cliente/MongoDB", MongoDB);