# ------------------------
#       VARIABLES
# ------------------------

#
# Variables: Canvas
#

# Nodos del canvas ordenados por capa
NodesByZIndex = []

# Canvas
canvas = document.getElementById 'canvas'
# Evento del canvas
canvas.onclick = null
canvas.ondoubleclick = false
canvas.onmouseup = null
canvas.onmousemove = null
# Contexto del canvas
context = document.getElementById 'context'
# Nombre del espacio del contexto del canvas
context.ns = 'http://www.w3.org/2000/svg'

#
# Variables: Configuración
#

# Tiempo máximo (en ms) entre dos eventos
# de click para considerarse dobleclick
doubleclickTimer = 300

#
# Variables: Modales
#

# Variable con toda la información necesaria
# sobre la ventana modal actual
currentModal =
    name: undefined
    opts: undefined

# Nombres de los modales existentes
modalName =
    new: 'modalNewNode'

# ------------------------
#       MÉTODOS
# ------------------------

#
# Métodos: Nodos
#

# Reordena los nodos según la disposición
# que tienen en el canvas.
reorderNodesByZIndex = ->
    # Función para comparar los zIndex
    comparator = (A,B) ->
        A.dom.style.zIndex > B.dom.style.zIndex
    # Ordenamos los nodos según su zIndex
    NodesByZIndex.sort comparator

# Obtiene el nodo superior al que apunta el ratón
getUpperNode = (coords) ->
    # Define el nodo superior
    upperNode = undefined
    # Reordenamos los nodos para asegurarnos de que
    # no haya fallos
    # HACK: Borrar para mejorar el rendimiento
    do reorderNodesByZIndex
    # Iteramos todos los nodos en orden descendente
    index = NodesByZIndex.length - 1 
    while not upperNode? and index >= 0
        # Obtenemos el elemento del DOM
        DOM = NodesByZIndex[index].dom
        # Comprobamos si el ratón está encima del DOM
        mouseIsOver = DOM.offsetLeft < coords.x < DOM.offsetLeft + DOM.offsetWidth
        mouseIsOver &= DOM.offsetTop < coords.y < DOM.offsetTop + DOM.offsetHeight
        # Guardamos el nodo si el ratón está encima
        upperNode = NodesByZIndex[index] if mouseIsOver
        # Decrementamos el contador
        index--
    # Devolvemos el nodo superior
    upperNode

# Obtiene todos aquellos nodos que no tienen entradas definidas
getStartNodes = ->
    # Definimos el resultado
    result = []
    # Guardamos aquellos nodos que no tengan entradas
    result.push node for node in NodesByZIndex when node.inputs.length is 0
    # Devolvemos el resultado
    result

# Obtiene los nodos conectados a la salida de un nodo
getOutputNodesFrom = (node) ->
    # Recorremos las salidas de los nodos
    result = []
    result.push output.to for output in node.outputs
    # Devolvemos el resultado
    result

# Añade un nuevo nodo al canvas
addNodeToCanvas = (node) ->
    # Añadimos el nuevo nodo al canvas
    do node.apppendOutput
    do node.move
    do node.show
    # Añadimos el nuevo nodo a la lista de nodos
    NodesByZIndex.push node

# Obtiene los nodos según su orden de ejecución y los devuelve por capas
# en un array bidimensional
getNodesByExecutionOrder = ->
    # Definimos el resultado
    result = []
    # Copiamos los nodos que existen en una piscina
    # de selección
    nodePool = do NodesByZIndex.slice
    # Creamos la primera capa seleccionando los nodos de inicio
    startNodes = do getStartNodes
    # Comprobamos si los existen nodos iniciales
    # y devolvemos error en caso de que no
    return false if startNodes.length is 0
    # Añadimos los nodos iniciales como primera capa
    # del resultado y los eliminamos de la piscina de selección
    result.push startNodes
    nodePool.splice nodePool.indexOf(node), 1 for node in startNodes
    # Comprobamos el resto de niveles...
    while nodePool.length isnt 0
        # Para ello, comprobamos las salidas de los padres
        nodesInNextLevel = []
        parents = result[result.length - 1]
        # Creamos un array con los posibles nodos del siguiente nivel
        possibleNodes = []
        for parent in parents
            # Eliminamos duplicados
            possibleNodes.concat getOutputNodesFrom(parent).filter (node) -> possibleNodes.indexOf(node) < 0
        # Comprobamos los requisitos, es decir, que las entradas
        # ya hayan sido valoradas
        for node in possibleNodes
            index = 0
            needMoreNodes = false
            while not needMoreNodes and index < child.inputs.length
                parent = child.inputs[index].path.from.parent
                needMoreNodes = nodePool.indexOf (parent) isnt -1
                index++
            # Comprobamos que no necesita más nodos
            if not needMoreNodes
                nodesInNextLevel.push node
                nodePool.splice nodePool.indexOf(node), 1
        # Comprobamos que no haya bucles infinitos
        return false if nodesInNextLevel.length is 0
        # Insertamos los nodos en el nuevo nivel
        result.push nodesInNextLevel
    # Si todo acaba correctamente, devolvemos los nodos agrupados por ejecución
    result

#
# Métodos: Paths
#

# Genera la definición de los caminos a partir de dos coordenadas
generatePath = (start,end) ->
    "M " + start.x + " " + start.y + " L " + end.x + " " + end.y

#
# Métodos: Ventanas modal
#

# Muestra una ventana modal según su nombre
showModal = (name) ->
    # Obtenemos la ventana modal según el nombre
    modal = document.getElementById name
    # Cambiamos la posición de la ventana
    modal.style.bottom = '20px' if modal?
    # No devolvemos nada
    return

# Oculta una ventana modal según su nombre
hideModal = (name) ->
    # Obtenemos la ventana modal según el nombre
    modal = document.getElementById name
    # Cambiamos la posición de la ventana
    modal.style.bottom = '-500px' if modal?
    # No devolvemos nada
    return

# Ejecuta el modal según su nombre y datos
runModal = (name,event,form) ->
    # Previene comportamientos estándar
    do event.preventDefault
    # Selecciona el comportamiento del modal
    switch name
        # Para nuevos nodos...
        when modalName.new then createNewNodeFromModal form.work.value
    # Oculta el modal
    hideModal name
    # Devuelve falso para prevenir comportamientos estándar
    false

# Ejecuta el modal de "Crear nodo"
createNewNodeFromModal = (work) ->
    # Obtenemos el nombre del nodo
    # en minúsculas y sin espacios
    work = do work.replace(/ /g, '-').toLowerCase
    # TODO: Implementar nuevo nodo
    node = switch work
        when "TODO" then "TODO"
        else "TODO"
    # Añadimos el nuevo nodo al canvas
    addNodeToCanvas node
    # No devolvemos nada
    return

#
# Métodos: Eventos del canvas
#

# Evento de click en el canvas
clickOnCavas = (coords) ->
    # Función para controlar el doble click
    timeout = -> canvas.ondoubleclick = false
    # Comprobamos si se ha hecho doble click
    if canvas.ondoubleclick
        # Comprobamos si se ha hecho
        # doble click encima de un nodo
        node = getUpperNode coords
        # Si no se ha hecho doble click en un nodo,
        # mostramos el modal de nuevo nodo
        if not node?
            currentModal =
                name: modalName.new
                opts: coords
            showModal currentModal.name
        # Si no, mostramos las opciones del nodo
        else showModal node.name
    # Si no se ha hecho doble click
    else
        # Ocultamos la ventana modal si hay
        hideModal currentModal.name if currentModal.name?
        # Iniciamos el evento de doble click
        canvas.ondoubleclick = true
        setTimeout timeout, doubleclickTimer
    # No devolvemos nada
    return
# Hacemos que sea el evento predeterminado al hacer click en el canvas
canvas.onclick = clickOnCavas



