# Variables

All the `global` variables **must** be defined in this file.

## 📜 Table of Contents
---
Related to:
1. [Arrays](#Arrays)
2. [Canvas](#Canvas)
4. [Modals](#Modals)

## 🧵 Related to
---
### Arrays

    # All nodes
    Nodes = []

### Canvas

    # Canvas Node Editor
    canvas = document.getElementById 'canvas'
    # Canvas double click flag
    canvas.doubleclick = false
    # Canvas events
    canvas.onclick = null
    canvas.onmouseup = null
    canvas.onmousemove = null
    # Canvas Context
    context = document.getElementById 'context'
    # Context Namespace
    context.ns = 'http://www.w3.org/2000/svg'
    # Double click Timer
    doubleClickTimer = 300

### Modals

    # Current visible Modal
    currentModal =
        name: undefined
        opts: undefined
