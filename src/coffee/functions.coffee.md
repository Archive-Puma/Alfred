    reorderByZIndex = (nodes) ->
        comparator = (nodeA, nodeB) ->
            nodeA.dom.style.zIndex > nodeB.dom.style.zIndex
        nodes.sort(comparator)