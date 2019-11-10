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

| Name | Arguments | Return | Description |
| --- | --- | --- | --- |
| createPath | [object] event | [boolean] `false` | Update the position of the Node in a smooth way using the mouse coordinates as a reference. |

        createPath = (event) ->
            #event.preventDefault()
            # If there is no path, creates a new one
            if not $.path
                $.path = document.createElementNS context.ns, 'path'
                $.path.setAttributeNS null, 'd', createPath
                    x: 0
                    y: 0,
                    x: event.pageX,
                    y: event.pageY
                context.appendChild $.path
            # Return (pevent defaults)
            event.stopPropagation() if event.stopPropagation
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