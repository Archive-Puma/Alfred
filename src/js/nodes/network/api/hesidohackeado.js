function HeSidoHackeado()
{
    this.demo_email = "correo@gmail.com";
    this.API = "https://haveibeenpwned.com/api/v2/breachedaccount/";

    this.email_widget = this.addWidget(
        "text",
        "Email",
        this.demo_email,
        function() {}
    )
    this.addInput("", LiteGraph.ACTION);
    this.addInput("Email", this.demo_email);
    this.addOutput("", LiteGraph.EVENT);
    this.addOutput("Resultado", undefined);
    this.addOutput("Cuentas hackeadas", undefined);
}

HeSidoHackeado.title = "¿He sido hackeado?";
HeSidoHackeado.desc = "Comprueba si un email ha sido hackeado mediante HIBP";

HeSidoHackeado.prototype.onAction = function()
{
    let input_email = this.getInputData(1);
    if(input_email !== undefined) {
        this.email_widget.value = input_email;
    }
    if(this.email_widget.value !== undefined
        && this.email_widget.value.constructor === String
        && this.email_widget.value.includes("@"))
    {
        this.checkEmail();
    } else { this.setOutputData(1, undefined); this.setOutputData(2, undefined); }
}

HeSidoHackeado.prototype.checkEmail = function()
{
    let that = this;
    let good_request = false;
    let email = this.email_widget.value;
    let xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", this.API.concat(email), true);
    xmlHttp.onloadend = function() {
        if(xmlHttp.readyState === 4 && xmlHttp.status === 200) {
            accounts = [];
            data = JSON.parse(xmlHttp.responseText);
            for(let service of data) { accounts.push(service.Name); }
            response = { result: true, accounts: accounts };
            good_request = true;
        } else if(xmlHttp.status === 404) {
            response = { result: false, accounts: undefined };
            good_request = true;
        }
        if(good_request) {
            that.setOutputData(1, response.result);
            that.setOutputData(2, response.accounts);
            that.triggerSlot(0, "haveibeenopwned");
        } else { that.setOutputData(1, undefined); that.setOutputData(2, undefined); }
    }
    xmlHttp.send(null);
}

LiteGraph.registerNodeType("API/¿He sido hackeado?", HeSidoHackeado);