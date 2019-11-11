# Methods

All the `global` methods **must** be defined in this file.

## 📜 Table of Contents
---
Related to:
1. [Nodes](#Nodes)

## 🧵 Related to
---
### Nodes

| Name | Arguments | Return | Description |
| --- | --- | --- | --- |
| reorderByZIndex | | [object] nodes | Reorder the `Nodes` by the Z-Index style property in ascendent order |

    reorderByZIndex = () ->
        # Comparator function
        comparator = (nodeA, nodeB) ->
            nodeA.dom.style.zIndex > nodeB.dom.style.zIndex
        # Sort the nodes
        Nodes.sort(comparator)

    getHoverNode = (mouse) ->
        # FIXME
        hoverNode = undefined
        index = Nodes.length
        while not hoverNode and index isnt 0
            index--
            dom = Nodes[index].dom
            hoverNode = Nodes[index] if dom.offsetLeft < mouse.x < dom.offsetLeft + dom.offsetWidth and dom.offsetTop < mouse.y < dom.offsetTop + dom.offsetHeight
        hoverNode


### Paths

| Name | Arguments | Return | Description |
| --- | --- | --- | --- |
| calculatePath | [object] start, [object] end | [string] path | Calculate the path between two points |

    calculatePath = (start, end) ->
        "M " + start.x + " " + start.y + " L " + end.x + " " + end.y