# Class: Ouput

An `Output Slot` is an entity that allows connect different `Nodes`.

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
| parent | object | `undefined` | The parent element of the current `Output` |

    Output = (@parent) ->
        # 'this' nickname
        $ = @

### Methods

| Name | Arguments | Return | Description |
| --- | --- | --- | --- |
| createPath | [object] event | [boolean] `false` | Create a new path from the selected output |

        createPath = (event) ->
            # Prevent defaults
            event.preventDefault()
            # Create the new path
            $.path = new Path $
            # Update the canvas events
            canvas.onmousemove = recalculatePath
            canvas.onmouseup = finishPath
            # Return (prevent defaults)
            event.stopPropagation()
            false

| Name | Arguments | Return | Description |
| --- | --- | --- | --- |
| recalculatePath | [object] event | [boolean] `false` | Update the path coordinates |

        recalculatePath = (event) ->
            # Prevent defaults
            event.preventDefault()
            # Update the path using the mouse coordinates
            $.path.updateMouseCoordinates().updateRoute()
            # Return (prevent defaults)
            event.stopPropagation()
            false

| Name | Arguments | Return | Description |
| --- | --- | --- | --- |
| finishPath | [object] event | [boolean] `false` | Connect the path to a node |

        finishPath = (event) ->
            # Prevent defaults
            event.preventDefault()
            # Update the canvas events
            canvas.onmouseup = null
            canvas.onmousemove = null
            # Get the node over the mouse
            hoverNode = getHoverNode
                x: event.pageX
                y: event.pageY
            # Append path to the node if exists
            if hoverNode
                hoverNode.inputs.push
                    element: $
                    path: $.path
                $.path.to = hoverNode
                # Update the route
                $.path.updateCoordinatesBetweenNodes().updateRoute()
            # Destroy the path if there is no node
            else $.path.destroy()
            # Return (prevent defaults)
            event.stopPropagation()
            false

### Variables

| Name | Type | Description |
| --- | --- | --- |
| dom | object | The DOM element |

        # DOM Element
        @dom = document.createElement 'div'
        @dom.classList.add 'output'
        @dom.onmousedown = createPath
        @parent.dom.appendChild @dom

### Return

| Name | Type | Description |
| --- | --- | --- |
| `this` | object | It is necessary for the class to return itself to concatenate functions. |

        @

## 🤖 Prototype
---

    Output.prototype =

| Name | Arguments | Return | Description |
| --- | --- | --- | --- |
| getCoordinates | [void] | [object] coordinates | Get the coordinates of the output |

        getCoordinates: () ->
            x: @dom.offsetParent.offsetLeft + @dom.offsetParent.offsetWidth + @dom.offsetWidth
            y: @dom.offsetParent.offsetTop + @dom.offsetParent.offsetHeight / 2