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
| reorderByZIndex | nodes | nodes | Reorder the `Nodes` by the Z-Index style property |

    reorderByZIndex = (nodes) ->
        comparator = (nodeA, nodeB) ->
            nodeA.dom.style.zIndex > nodeB.dom.style.zIndex
        nodes.sort(comparator)