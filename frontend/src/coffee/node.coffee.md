# Class: Node

A `Node` is an entity that contains all the information of a `Task`.

## 📜 Table of Contents
---
1. [Constructor](#Constructor)
2. [Methods](#Methods)
3. [Variables](#Variables)
4. [Return](#Return)
5. [Prototype](#🤖-Prototype)

## 🏷️ Definition
---

### Constructor

Special type of subroutine called to create an `Object`.

Arguments:

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| work | string | `undefined` | Work type |
| pos | object | `{ x: 0, y: 0 }` | Position of the visual DOM element |

    Node = (@work, pos) ->
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
            # Double click event
            if $.doubleclicked
                # Show the modal with the options
                $.showModalOpts()
            else
                # Update the canvas events
                canvas.onmousemove = move
                canvas.onmouseup = undrag
                # Update the double click event
                $.doubleclicked = true
                doubleclickEvent = -> $.doubleclicked = false
                setTimeout doubleclickEvent, doubleClickTimer
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
            # Update the inputs
            input.path.updateCoordinatesBetweenNodes().updateRoute() for input in $.inputs
            # Update the outputs
            outpath.updateCoordinatesBetweenNodes().updateRoute() for outpath in $.outputs
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
| icon | string | `undefined` | Icon belonging to the FontAwesome library |
| ppos | object | The last position of the DOM element |
| dom | object | The DOM element |
| child | object | The output slot |
| inputs | object | All the input paths |
| outputs | object | All the output paths |
| doubleclicked | boolean | Double click flag | 

        # Icon
        @icon = switch @work
            when 'port-scan'    then 'sitemap'
            when 'whois'        then 'radiation'
            else 'file'
        # Double clicked
        @doubleclicked = false
        # Last position
        @ppos = @pos
        # The output slot
        @child = undefined
        # Path variables
        @inputs = []
        @outputs = []
        # DOM Element
        @dom = document.createElement 'div'
        @dom.classList.add 'node', 'fas', 'fa-' + @icon
        @dom.style.zIndex = Nodes.length + 10
        @dom.onmousedown = drag
        # Modal
        @modal = undefined

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
            new Output @
            # Return itself to concatenate functions
            @

| Name | Arguments | Return | Description |
| --- | --- | --- | --- |
| move | [void] | [object] `this` | Translate the node to the new position |

        move: () ->
            @dom.style.left = @pos.x + 'px'
            @dom.style.top = @pos.y + 'px'
            # Return itself to concatenate functions
            @

| Name | Arguments | Return | Description |
| --- | --- | --- | --- |
| setModal | [string] name | [object] `this` | Set the linked modal |

        setModal: (name) ->
            @modal = document.getElementById "modal" + name
            # Return itself to concatenate functions
            @

| Name | Arguments | Return | Description |
| --- | --- | --- | --- |
| showModalOpts | [void] | [object] `this` | Display the linked modal |

        showModalOpts: () ->
            # Hide the displayed modal
            hideModal currentModal.name if currentModal.name?
            # Show the modal with the options
            currentModal =
                name: @modal.id
                opts: undefined
            showModal currentModal.name
            # Return itself to concatenate functions
            @
