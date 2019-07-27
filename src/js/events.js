function mousePressed()
{
    var index = 0;
    var item = undefined;
    while(!item && index < Nodes.length)
    {
        var node = Nodes[index];
        var distance = dist(mouseX,mouseY, node.position.x, node.position.y);
        if(distance <= node.radius)
        {
            item = node;
            node.selected = true;
        }

        index++;
    }

    if(item)
    {
        if(SelectedNode === item)  { SelectedNode.writing = true; }
        else {
            if(keyIsDown(SHIFT)) { Links.push(new Link(SelectedNode, item)); }
            releaseNode();
            SelectedNode = item;
        }
    } else {
        if(SelectedNode) {
            if(keyIsDown(SHIFT))
            {
                var node = SelectedNode;
                createNode(mouseX, mouseY);
                Links.push(new Link(node, SelectedNode));
            } else { releaseNode(); }
        } else {
            if(dist(mouseX,mouseY,lastClick.x, lastClick.y) < 1)
            {
                createNode(mouseX,mouseY);
            }
        }
    }

    lastClick = createVector(mouseX,mouseY);
}

function mouseDragged()
{
    if(SelectedNode)
    {
        SelectedNode.position = createVector(mouseX, mouseY);
    }
}

function keyReleased()
{
    if(SelectedNode)
    {
        var lowerkey = key.toLowerCase();
        if(SelectedNode.writing)
        {
            if(key.length === 1)
            {
                SelectedNode.code += key;
            } else
            {
                if(lowerkey === "backspace")
                {
                    SelectedNode.code = SelectedNode.code.slice(0,-1);
                } else if(lowerkey === "enter")
                {
                    SelectedNode.writing = false;
                }
            }
        }

        if(lowerkey === "delete")
        {
            var node = SelectedNode;
            var index = Nodes.indexOf(node);
            if(index !== -1)
            {
                releaseNode();
                lastClick = createVector(-1,-1);
                Nodes.splice(index, 1);

                var i = 0;
                while(i < Links.length)
                {
                    var link = Links[i];
                    if(link.from.id === node.id ||
                        link.to.id === node.id)
                    {
                        Links.splice(i, 1);
                    } else { i++; }
                }
            }
        }
    } 

    return false;
}
