# Class: Ouput

An `Output Slot` is an entity that allows connect different `Nodes`.

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

    Output = () ->
        $ = @

### Methods

        detachPath = () ->
            context.removeChild $.path
            $.path = undefined

| Name | Arguments | Return | Description |
| --- | --- | --- | --- |
| createPath | [object] event | [boolean] `false` | Update the position of the Node in a smooth way using the mouse coordinates as a reference. |

        createPath = (event) ->
            event.preventDefault()
            detachPath $.path if $.path
            # Create the new path
            route = calculatePath $.getCoordinates(),
                x: event.pageX
                y: event.pageY
            $.path = document.createElementNS context.ns, 'path'
            $.path.setAttributeNS null, 'd', route
            context.appendChild $.path
            # Update the canvas events
            canvas.onmousemove = recalculatePath
            canvas.onmouseup = finishPath
            # Return (prevent defaults)
            event.stopPropagation()
            false

        recalculatePath = (event) ->
            event.preventDefault()
            # If there is no path, creates a new one
            route = calculatePath $.getCoordinates(),
                    x: event.pageX
                    y: event.pageY
            $.path.setAttribute('d', route)
            # Return (prevent defaults)
            event.stopPropagation()
            false

        finishPath = (event) ->
            event.preventDefault()
            # Update the canvas events
            canvas.onmouseup = null
            canvas.onmousemove = null
            hoverNode = getHoverNode
                x: event.pageX
                y: event.pageY
            if hoverNode
                $.path.setAttribute 'd', calculatePath $.getCoordinates(),
                    x: hoverNode.dom.offsetLeft
                    y: hoverNode.dom.offsetTop + hoverNode.dom.offsetHeight / 2
            else detachPath $.path
            # Return (prevent defaults)
            false
### Variables

| Name | Type | Description |
| --- | --- | --- |
| dom | object | The DOM element |

        # DOM Element
        @dom = document.createElement 'div'
        @dom.classList.add 'output'
        @dom.onmousedown = createPath

### Return

        @

## 🤖 Prototype
---

| Name | Arguments | Return | Description |
| --- | --- | --- | --- |
| show | | [object] `this` | Append the DOM element to the canvas |

    Output.prototype =
        getCoordinates: () ->
            x: @dom.offsetParent.offsetLeft + @dom.offsetParent.offsetWidth + @dom.offsetWidth
            y: @dom.offsetParent.offsetTop + @dom.offsetParent.offsetHeight / 2