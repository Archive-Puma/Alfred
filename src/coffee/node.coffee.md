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
| icon | String | `undefined` | Icon belonging to the FontAwesome library |
| pos | Object | `{ x: 0, y: 0 }` | Position of the DOM visual element |

    Node = (@icon, pos) ->
        $ = @
        @pos = pos or
            x: 0
            y: 0

### Methods

        move = (event) ->
            $.pos =
                x: $.ppos.x - event.clientX
                y: $.ppos.y - event.clientY
            $.ppos =
                x: event.clientX
                y: event.clientY
            $.dom.style.left = ($.dom.offsetLeft - $.pos.x) + 'px'
            $.dom.style.top = ($.dom.offsetTop - $.pos.y) + 'px'

##

        undrag = (event) ->
            canvas.onmouseup = null
            canvas.onmousemove = null
            $.dom.style.zIndex = 9
            Nodes = reorderByZIndex Nodes
            node.dom.style.zIndex = index + 10 for node, index in Nodes

##

        drag = (event) ->
            $.dom.style.zIndex = Nodes.length + 10;
            $.ppos =
                x: event.clientX
                y: event.clientY
            canvas.onmousemove = move
            canvas.onmouseup = undrag

### Variables

        @ppos = @pos
        # DOM Element
        @dom = document.createElement 'div'
        @dom.classList.add 'node', 'fas', 'fa-' + @icon
        @dom.style.zIndex = Nodes.length + 10
        @dom.onmousedown = drag

### Return

        @

## 🤖 Prototype
---

    Node.prototype =
        show: () ->
            canvas.appendChild @dom
            @
        appendOutput: () ->
            @