# Methods

All the `global` methods **must** be defined in this file.

## 📜 Table of Contents
---
Related to:
1. [Nodes](#Nodes)
2. [Paths](#Paths)
3. [Canvas](#Canvas)
4. [Modals](#Modals)

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

| Name | Arguments | Return | Description |
| --- | --- | --- | --- |
| getNodesByExecution | [void] | [object] nodes | Get all the Nodes following their outputs |

    getNodesByExecution = () ->
        nodesPool = Nodes.slice()
        nodesByExecution = []
        # First layer, starting nodes
        nodesByExecution.push getStartNodes()
        # Check the length
        return false if nodesByExecution[0].length is 0
        # Remove starting nodes from the pool
        nodesPool.splice nodesPool.indexOf(startingNode), 1 for startingNode in nodesByExecution[0]
        # Check the rest of the levels
        while nodesPool.length != 0
            # From selected nodes in the last level...
            for parent in nodesByExecution[nodesByExecution.length - 1]
                # Create the new level
                nextLevel = []
                # Check all this childs
                for output in parent.outputs
                    # Get the child
                    child = output.to
                    # Check the requisites (variables)
                    i = 0
                    needMore = false
                    # Check the requisites (algorithm) - All parents computed
                    while not needMore and i < child.inputs.length
                        connectedFrom = child.inputs[i].path.from.parent
                        needMore = nodesPool.indexOf(connectedFrom) != - 1
                        needMore ||= nextLevel.indexOf(connectedFrom) != -1
                        i = i + 1
                    # Check the requisites (result?)
                    if not needMore
                        nextLevel.push child
                        nodesPool.splice(nodesPool.indexOf(child), 1)
            # Check if the level has any node (no loops)
            return false if nextLevel.length is 0
            # Insert the level in the list
            nodesByExecution.push nextLevel
        # All correctly done
        nodesByExecution

### Paths

| Name | Arguments | Return | Description |
| --- | --- | --- | --- |
| calculatePath | [object] start, [object] end | [string] path | Calculate the path between two points |

    calculatePath = (start, end) ->
        "M " + start.x + " " + start.y + " L " + end.x + " " + end.y

### Canvas

| Name | Arguments | Return | Description |
| --- | --- | --- | --- |
| createNewNode | [object] event | [void] | Create a new Node by double-clicking |

    createNewNode = (event) ->
        # Timeout function
        timeout = () -> canvas.doubleclick = false
        # Check the state of the flag
        if canvas.doubleclick
            # Show the needed modal
            hoverNode = getHoverNode
                x: event.pageX
                y: event.pageY
            # New node
            if not hoverNode?
                currentModal =
                    name: 'modalNewNode'
                    opts:
                        x: event.pageX
                        y: event.pageY
                showModal currentModal.name
            # Node options
            else
                showModal hoverNode.icon
        else
            # Hide modal
            hideModal currentModal.name if currentModal?
            # Set flag to true and start a timeout
            canvas.doubleclick = true
            setTimeout timeout, doubleClickTimer
        # Return void
        return
    canvas.onclick = createNewNode

### Modals

| Name | Arguments | Return | Description |
| --- | --- | --- | --- |
| showModal | [string] name | [void] | Show a modal dialog |

    # Show Modal
    showModal = (name) ->
        if name?
            modal = document.getElementById name
            modal.style.bottom = '20px' if modal?
        return

| Name | Arguments | Return | Description |
| --- | --- | --- | --- |
| hideModal | [string] name | [void] | Hide a modal dialog |

    hideModal = (name) ->
        if name?
            modal = document.getElementById name
            modal.style.bottom = '-500px' if modal?
        return

| Name | Arguments | Return | Description |
| --- | --- | --- | --- |
| runModal | [object] event | [boolean] false | Model callback: Create a new Node |

    runModal = (name,event,form) ->
        # Prevent defaults
        event.preventDefault()
        if name is 'modalNewNode'
            # Format the work name
            name = form.work.value.toLowerCase().replace(/ /g,'-')
            # Create the new node
            node = switch name
                when 'port-scan' then PortScan currentModal.opts
                else new Node name, currentModal.opts
            node.appendOutput().move().show()
            Nodes.push node
        # Hide the modal
        hideModal currentModal.name
        # Return (prevent defaults)
        false