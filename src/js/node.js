function Node(position)
{
    this.gap = radians(10);
    this.code = "";
    this.writing = false;
    this.radius = 30;
    this.selected = false;
    this.position = position;
    this.color = {
        in: color(100), out: color(200),
        writing: color(150,200,60),
        selected: color(255), text: color(200)
    };

    this.empty = function()
    {
        return this.code.length === 0;
    }


    this.draw = function()
    {
        noFill();
        strokeWeight(2);

        stroke(this.color.in);
        arc(this.position.x, this.position.y,
            this.radius, this.radius,
            HALF_PI + this.gap, HALF_PI + PI - this.gap,
            OPEN);

        stroke(this.color.out);
        arc(this.position.x, this.position.y,
            this.radius, this.radius,
            HALF_PI + PI + this.gap, HALF_PI - this.gap,
            OPEN);

        if(this.selected)
        {
            var remark = this.writing ? this.color.writing : this.color.selected;
            stroke(remark);
            circle(this.position.x, this.position.y, this.radius + 20, this.radius + 20);
        }
        
        if(!this.empty())
        {
            noStroke();
            fill(this.color.text);
            text(this.code, this.position.x, this.position.y - this.radius * 1.1);
        }

        if(this.show) { this.show(); }
    }
}

function createStartNode()
{
    var position = createVector(56,111);
    var node = new Node(position);
    node.code = "Inicio";
    node.show = function()
    {
        fill(255);
        noStroke();
        ellipse(this.position.x, this.position.y,
            this.radius / 2.5, this.radius / 2.5);
    }
    appendNode(node);
}

function createNode(x,y)
{
    var position = createVector(x,y);
    var node = new Node(position);
    releaseNode();
    node.writing = true;
    node.selected = true;
    SelectedNode = node;
    appendNode(node);
}

function appendNode(node)
{
    node.id = Nodes.length === 0 ? 0 : Nodes[Nodes.length - 1].id + 1;
    Nodes.push(node);
    console.log(Nodes);
}

function binaryGetNode(id)
{
    var wanted;
    var min = 0;
    var max = Nodes.length - 1;
    while(!wanted && min <= max)
    {
        var mid = Math.floor((max + min) / 2);
        var node = Nodes[mid];
        if(node.id === id) { wanted = node; }
        else if(node.id > id) { max = mid - 1; }
        else { min = mid + 1; }
    }
    
    return wanted;
}

function releaseNode()
{
    if(SelectedNode)
    {
        SelectedNode.writing = false;
        SelectedNode.selected = false;
        SelectedNode = undefined;
    }
}