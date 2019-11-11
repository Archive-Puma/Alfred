# Class: Node

A `Node` is an entity that contains all the information of a `Task`.

## 📜 Table of Contents
---
1. [Constructor](#Constructor)
2. [Methods](#Methods)
3. [Variables](#Variables)
4. [Return](#Return)
5. [Prototype](#Prototype)

## 🏷️ Definition
---

### Constructor

Special type of subroutine called to create an `Object`.

Arguments:

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| icon | string | `undefined` | Icon belonging to the FontAwesome library |
| pos | object | `{ x: 0, y: 0 }` | Position of the visual DOM element |

    Node = (@icon, pos) ->
        # 'this' nickname
        $ = @
        # Default argument values
        @pos = pos or
            x: 0
            y: 0

### Methods

| Name | Arguments | Return | Description |
| --- | --- | --- | --- |
| drag | [object] event | [boolean] `false` | Start the drag event. |

        drag = (event) ->
            # Prevent defaults
            event.preventDefault()
            # Update the Z-Index of the selected Node
            $.dom.style.zIndex = Nodes.length + 10;
            # Update the last position of the Node
            $.ppos =
                x: event.clientX
                y: event.clientY
            # Update the canvas events
            canvas.onmousemove = move
            canvas.onmouseup = undrag
            # Return (prevent defaults)
            false

| Name | Arguments | Return | Description |
| --- | --- | --- | --- |
| move | [object] event | [boolean] `false` | Update the position of the Node in a smooth way using the mouse coordinates as a reference. |

        move = (event) ->
            # Prevent defaults
            event.preventDefault()
            # Calculate the new position in a smooth way
            $.pos =
                x: $.ppos.x - event.clientX
                y: $.ppos.y - event.clientY
            # Update the last position of the Node
            $.ppos =
                x: event.clientX
                y: event.clientY
            # Update the position of the DOM element
            $.dom.style.left = ($.dom.offsetLeft - $.pos.x) + 'px'
            $.dom.style.top = ($.dom.offsetTop - $.pos.y) + 'px'
            # Update inputs
            for path in $.inputs
                # Calculate and update the new path
                route = path.getAttribute('d').split(" L ")[0] + " L " + $.dom.offsetLeft + " " + ($.dom.offsetTop + $.dom.offsetHeight/2)
                path.setAttribute('d', route)
            # Update outputs (FIXME pls)
            for out in $.outputs
                # Check if output and path exist
                if out and out.path
                    # Get the output coordinates
                    pos = out.getCoordinates()
                    # Calculate and update the new path
                    route = "M " + pos.x + " " + pos.y + " L " + out.path.getAttribute('d').split(" L ")[1]
                    out.path.setAttribute('d', route)
            # Return (prevent defaults)
            event.stopPropagation()
            false

| Name | Arguments | Return | Description |
| --- | --- | --- | --- |
| undrag | [object] event | [boolean] `false` | End the drag event and update the visual layout of the layers. |

        undrag = (event) ->
            # Prevent defaults
            event.preventDefault()
            # Unset the canvas events
            canvas.onmouseup = null
            canvas.onmousemove = null
            # Update the Z-Index of the selected Node
            $.dom.style.zIndex = 9
            # Reorder nodes by Z-Index
            Nodes = reorderByZIndex Nodes
            node.dom.style.zIndex = index + 10 for node, index in Nodes
            # Return (prevent defaults)
            false

### Variables

| Name | Type | Description |
| --- | --- | --- |
| ppos | object | The last position of the DOM element |
| dom | object | The DOM element |
| inputs | object | All the input paths |
| outputs | object | All the output slots |

        # Last position
        @ppos = @pos
        # Slot variables
        @inputs = []
        @outputs = []
        # DOM Element
        @dom = document.createElement 'div'
        @dom.classList.add 'node', 'fas', 'fa-' + @icon
        @dom.style.zIndex = Nodes.length + 10
        @dom.onmousedown = drag

### Return

| Name | Type | Description |
| --- | --- | --- |
| `this` | object | It is necessary for the class to return itself to concatenate functions. |

        @

## 🤖 Prototype
---

    Node.prototype =

| Name | Arguments | Return | Description |
| --- | --- | --- | --- |
| show | [void] | [object] `this` | Append the DOM element to the canvas |

    
        show: () ->
            # Append the Node to the Canvas
            canvas.appendChild @dom
            # Return itself to concatenate functions
            @

| Name | Arguments | Return | Description |
| --- | --- | --- | --- |
| appendOutput | [void] | [object] `this` | Append an output slot to the `Node` |

        appendOutput: () ->
            # Append an Output to the Node
            @outputs.push new Output @
            # Return itself to concatenate functions
            @