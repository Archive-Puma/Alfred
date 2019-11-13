# Methods

All the `global` methods **must** be defined in this file.

## 📜 Table of Contents
---
Related to:
1. [Nodes](#Nodes)
2. [Paths](#Paths)

## 🧵 Related to
---

### Nodes

| Name | Arguments | Return | Description |
| --- | --- | --- | --- |
| reorderByZIndex | [void] | [object] nodes | Reorder the `Nodes` by the Z-Index style property in ascendent order |

    reorderByZIndex = () ->
        # Comparator function
        comparator = (nodeA, nodeB) ->
            nodeA.dom.style.zIndex > nodeB.dom.style.zIndex
        # Sort the nodes
        Nodes.sort(comparator)

| Name | Arguments | Return | Description |
| --- | --- | --- | --- |
| getHoverNode | [object] mouse | [object] node / `undefined` | Get the first node the mouse points to |

    getHoverNode = (mouse) ->
        # Define the hoverNode
        hoverNode = undefined
        # Iterate in descending order until a Node is selected
        index = Nodes.length
        while not hoverNode and index isnt 0
            index--
            dom = Nodes[index].dom
            # Check if a the mouse is over a Node
            hoverNode = Nodes[index] if dom.offsetLeft < mouse.x < dom.offsetLeft + dom.offsetWidth and dom.offsetTop < mouse.y < dom.offsetTop + dom.offsetHeight
        # Return the Node if the mouse points to it
        hoverNode

| Name | Arguments | Return | Description |
| --- | --- | --- | --- |
| getStartNodes | [void] | [object] nodes | Get all the Nodes without inputs |

    getStartNodes = () ->
        # Define the result array
        nodes = []
        # Iterate in order finding all the start nodes
        nodes.push node for node in Nodes when node.inputs.length is 0
        # Return the starting nodes
        nodes

### Paths

| Name | Arguments | Return | Description |
| --- | --- | --- | --- |
| calculatePath | [object] start, [object] end | [string] path | Calculate the path between two points |

    calculatePath = (start, end) ->
        "M " + start.x + " " + start.y + " L " + end.x + " " + end.y