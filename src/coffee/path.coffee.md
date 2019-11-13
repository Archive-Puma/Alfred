# Class: Ouput

A `Path` is an entity that connect two different `Slots`.

## 📜 Table of Contents
---
1. [Constructor](#Constructor)
2. [Variables](#Variables)
3. [Return](#Return)
4. [Prototype](#🤖-Prototype)

## 🏷️ Definition
---

### Constructor

Special type of subroutine called to create an `Object`.

Arguments:

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| from | object | `undefined` | The output `Slot` of a `Node` |
| to | object | `undefined` | The input `Slot` of a `Node` |

    Path = (@from, to) ->
        # 'this' nickname
        $ = @
        # Default argument values
        @to = to or undefined

### Methods

| Name | Arguments | Return | Description |
| --- | --- | --- | --- |
| removePath | [object] event | [boolean] `false` | Create a new path from the selected output |

        removePath = (event) ->
            # Prevent defaults
            event.preventDefault()
            # Destroy the path
            $.destroy()
            # Return (prevent defaults)
            event.stopPropagation()
            false

### Variables

| Name | Type | Description |
| --- | --- | --- |
| coordinates | object | From/To coordinates of the route |
| dom | object | The DOM element |

        # Coordinates
        @coordinates =
            from:
                x: 0
                y: 0
            to:
                x: 0
                y: 0
        # Add the path to the original Node
        @from.parent.outputs.push @
        # DOM Element
        @dom = document.createElementNS context.ns, 'path'
        @dom.onclick = removePath
        @updateCoordinatesBetweenNodes().updateRoute()
        context.appendChild @dom

### Return

| Name | Type | Description |
| --- | --- | --- |
| `this` | object | It is necessary for the class to return itself to concatenate functions. |

        @

## 🤖 Prototype
---

    Path.prototype =
    
| Name | Arguments | Return | Description |
| --- | --- | --- | --- |
| getRoute | [void] | [string] route | Create the route between two points |
    
        getRoute: () ->
            "M " + @coordinates.from.x + " " + @coordinates.from.y +
            " L " + @coordinates.to.x + " " + @coordinates.to.y

| Name | Arguments | Return | Description |
| --- | --- | --- | --- |
| updateRoute | [void] | [object] `this` | Update the route using the given coordinates |
    
        updateRoute: () ->
            # Update the route
            @.dom.setAttributeNS null, 'd', @getRoute()
            # Return itself to concatenate functions
            @

| Name | Arguments | Return | Description |
| --- | --- | --- | --- |
| updateCoordinatesBetweenNodes | [void] | [object] `this` | Create the route between two `Nodes` |
    
        updateCoordinatesBetweenNodes: () ->
            # Update the coordinates of the output
            @coordinates.from = @from.getCoordinates()
            # Update the coordinates of the input
            @coordinates.to =
                x: @to.dom.offsetLeft if @to
                y: @to.dom.offsetTop + @to.dom.offsetHeight / 2 if @to
            # Return itself to concatenate functions
            @
        
| Name | Arguments | Return | Description |
| --- | --- | --- | --- |
| updateMouseCoordinates | [object] event | [object] `this` | Create the route between a `Node` and the mouse |
    
        updateMouseCoordinates: () ->
            # Update the coordinates of the mouse
            @coordinates.to =
                x: event.pageX
                y: event.pageY
            # Return itself to concatenate functions
            @

| Name | Arguments | Return | Description |
| --- | --- | --- | --- |
| destroy | [void] | [void] | Detach the `Path` from the `Nodes` and destroy it |
    
        destroy: () ->
            # Remove the DOM
            @dom.removeAttributeNS null, 'd'
            context.removeChild @dom
            # Remove from the connected Node
            @from.parent.outputs.splice(index, 1) for index, output in @from.parent.outputs when output = @
            @to.inputs.splice(index, 1) for index, input in @to.inputs when input.path = @ if @to
            # Remove from the output
            @from.path = undefined
            # Return void
            return