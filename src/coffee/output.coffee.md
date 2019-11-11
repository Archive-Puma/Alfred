# Class: Ouput

An `Output Slot` is an entity that allows connect different `Nodes`.

## 📜 Table of Contents
---
1. [Constructor](#Constructor)
2. [Methods](#Methods)
3. [Variables](#Variables)

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
            start =
                x: $.dom.offsetParent.offsetLeft + $.dom.offsetParent.offsetWidth + $.dom.offsetWidth / 2
                y: $.dom.offsetParent.offsetTop + $.dom.offsetParent.offsetHeight / 2
            route = calculatePath start,
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
            start =
                x: $.dom.offsetParent.offsetLeft + $.dom.offsetParent.offsetWidth + $.dom.offsetWidth
                y: $.dom.offsetParent.offsetTop + $.dom.offsetParent.offsetHeight / 2
            route = calculatePath start,
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
                console.log("Hi")
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