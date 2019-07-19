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
        else { releaseNode(); SelectedNode = item; }
    } else {
        if(SelectedNode) {
            releaseNode();
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

function mouseReleased()
{
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
            var index = Nodes.indexOf(SelectedNode);
            if(index !== -1)
            {
                releaseNode();
                lastClick = createVector(-1,-1);
                Nodes.splice(index, 1);
            }
        }
    } 

    return false;
}
