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
    }
}

function createNode(x,y)
{
    var position = createVector(x,y);
    var node = new Node(position);
    releaseNode();
    node.writing = true;
    node.selected = true;
    SelectedNode = node;
    Nodes.push(node);
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