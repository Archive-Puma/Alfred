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
        $ = @
        @pos = pos or
            x: 0
            y: 0

### Methods

| Name | Arguments | Return | Description |
| --- | --- | --- | --- |
| drag | [object] event | [boolean] `false` | Start the drag event. |

        drag = (event) ->
            event.preventDefault()
            $.dom.style.zIndex = Nodes.length + 10;
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
            event.preventDefault()
            # Calculate the new position in a smooth way
            $.pos =
                x: $.ppos.x - event.clientX
                y: $.ppos.y - event.clientY
            # Update the last position
            $.ppos =
                x: event.clientX
                y: event.clientY
            # Update the position of the DOM element
            $.dom.style.left = ($.dom.offsetLeft - $.pos.x) + 'px'
            $.dom.style.top = ($.dom.offsetTop - $.pos.y) + 'px'
            # Update inputs
            for path in $.inputs
                route = path.getAttribute('d').split(" L ")[0] + " L " + $.dom.offsetLeft + " " + ($.dom.offsetTop + $.dom.offsetHeight/2)
                path.setAttribute('d', route)
            # Return (prevent defaults)
            event.stopPropagation()
            false

| Name | Arguments | Return | Description |
| --- | --- | --- | --- |
| undrag | [object] event | [boolean] `false` | End the drag event and update the visual layout of the layers. |

        undrag = (event) ->
            event.preventDefault()
            canvas.onmouseup = null
            canvas.onmousemove = null
            $.dom.style.zIndex = 9
            Nodes = reorderByZIndex Nodes
            node.dom.style.zIndex = index + 10 for node, index in Nodes
            # Return (rpevent defaults)
            false

### Variables

| Name | Type | Description |
| --- | --- | --- |
| ppos | object | The las position of the DOM element |
| dom | object | The DOM element |

        @ppos = @pos
        @inputs = []
        # DOM Element
        @dom = document.createElement 'div'
        @dom.classList.add 'node', 'fas', 'fa-' + @icon
        @dom.style.zIndex = Nodes.length + 10
        @dom.onmousedown = drag

### Return

It is necessary for the class to return itself to concatenate functions.

        @

## 🤖 Prototype
---

| Name | Arguments | Return | Description |
| --- | --- | --- | --- |
| show | | [object] `this` | Append the DOM element to the canvas |

    Node.prototype =
        show: () ->
            canvas.appendChild @dom
            @

| Name | Arguments | Return | Description |
| --- | --- | --- | --- |
| appendOutput |  | [object] `this` | Append an output `Slot` to the `Node` |

        appendOutput: () ->
            new Output @
            @