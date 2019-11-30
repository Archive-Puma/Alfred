# Electron Desktop App

Electron basic configuration to run `Alfred` as a Desktop Application.

## 📜 Table of Contents
---
1. [Modules](#Modules)
2. [Configuration](#Configuration)
3. [Variable](#Variable)
4. [Window](#Window)
5. [Events](#Events)

## Modules
---

Import the `electron` module like any other **NodeJS** module and initialize it.
`app` will allow us to control the application and `BrowserWindow` will be the window builder.

    # Import the electron module
    electron = require 'electron'
    # Initialize the module
    { app, BrowserWindow, Menu } = require 'electron'

## Configuration
---

Some window configuration before the creation.

    # Remove the Menu Bar
    Menu.setApplicationMenu null

## Variables
---

We need a variable that allows us to manage the active window at all times.

    # Active window
    window = null

## Window
---

Initialize the window with some parameters, such as size or integration with NodeJS.

> ⚠️ Activating the `nodeIntegration` parameter can lead to security problems, so you have to be cautious when using it.

| Name | Arguments | Return | Description |
| --- | --- | --- | --- |
| createWindow | [void] | [void] | Initialize and configure a window |

    createWindow = ->
        # Create the new active window
        window = new BrowserWindow
            show: false
            width: 800
            height: 600
            webPreferences:
                nodeIntegration: true
        # Load the .html file
        #window.loadFile 'index.html'
        window.loadFile 'dist/index.html'
        # Uncomment if we need the DevTools
        #window.webContents.openDevTools()
        # Run the window in maximize mode
        window.maximize()
        # Show the window
        window.show()
        # Return nothing
        return

## Events
---

It is necessary to handle some events such as "close the window" or some more specific ones such as the interaction with the `Dock` in `MacOS`.

| Name | Target | Event |
| --- | --- | --- |
| closed | window | Event related to the closing of the window (it belongs to the creation function) |

        window.on 'closed', ->
            # Delete the active window reference
            window = null
            # Return nothing
            return

| Name | Target | Event |
| --- | --- | --- |
| ready | app | This method will be called when `Electron` has finished initialization and is ready to create browser windows |

    # When the application is ready...
    app.on 'ready', createWindow

| Name | Target | Event |
| --- | --- | --- |
| activate | app | In `MacOS` it is common to recreate a window in the application when the `Dock` icon is clicked and there are no other windows open |

    # When the application is reactivated in MacOS...
    app.on 'activate', ->
        # Re-create the window
        createWindow() if window is null
        # Return nothing
        return

| Name | Target | Event |
| --- | --- | --- |
| window-all-closed | app | Event related to the closing of all windows |

    # When all windows are closed...
    app.on 'window-all-closed', ->
        # Close the process
        app.quit()