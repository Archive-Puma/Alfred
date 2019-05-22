===============
Lenguaje Alfred
===============

A pesar de que Alfred es un lenguaje bastante flexible estructuralmente, sigue
ciertas directrices a la hora de interpretar el código fuente de los programas.

Además, por convenio, todos los archivos que incluyan código fuente escrito en
este lenguaje de programación deberán tener la extensión ``.alf``.

Alfred
======

El archivo que contenga el flujo principal del programa ha de comenzar
obligatoriamente con la palabra reservada ``Alfred``. Además, esta palabra ha de
ser única en todo el código fuente.

Cualquier otra instrucción que preceda a dicha palabra reservada generará un
error de sintaxis parecido a este:

.. code-block::

  [🐛] (Línea: 1) Sintaxis inválida: ...

De este modo, si se desea generar un programa ``.alf`` vacío, el contenido será
similar a este:

.. code-block::

  Alfred.

Comentarios
===========

Como casi cualquier otro lenguaje de programación, Alfred acepta la inclusión de
comentarios en el código. Aunque la semántica sea más que expresiva, en muchas
ocasiones es recomendable, por no decir necesario, el uso de anotaciones.

Para ello, se disponen de los símbolos ``(`` y ``)``, los cuales encapsularán
cualquier contenido que será ignorado a la hora de procesar el código.

.. code-block::

  (Los comentarios pueden ir precediendo a la palabra reservada Alfred)

  Alfred. (También pueden ir intercalados entre instrucciones) Di "Buenos días, Sr. Wayne".

  (Además, Alfred acepta comentarios
  multilínea sin la necesidad de
  caracteres especiales adicionales)

.. WARNING::

  Hay que tener cuidado al comentar código. La ausencia de un paréntesis puede
  convertir tus instrucciones en simples anotaciones.

.. code-block::

  Alfred.
  Di "Esto no es un comentario".
  (Hay que intentar no olvidarse de cerrar los comentarios
  Di "Esto es parte del comentario"
  (Alfred ignorará cualquier código si éste es tratado como un comentario)
  Di "Esto tampoco es parte de un comentario".

La ausencia de un paréntesis, es decir, si la cantidad total de pares de
paréntesis es impar, Alfred generará una excepción similar a esta:

.. code-block::

  [🐛] Caracter inválido (1,~184): (

Instrucciones
=============

Di
--

La instrucción ``Di`` permite mostrar un texto por pantalla. Cualquier argumento
que se le pase será propiamente tratado para que se pueda mostrar por la salida
estándar del sistema. Además, un nuevo salto de línea será añadido tras evaluar
la instrucción.

.. code-block::

  Alfred. Di "Encantado de conocerte, Batman".

**Resultado**:
  .. code-block::

    Encantado de conocerte, Batman

.. ATTENTION::

  Los caracteres escapados tales como ``\n``, ``\r`` o ``\t`` **son tratados
  de manera literal**, por lo que si deseas que se muestren por pantalla,
  sólamente has de usarlos como si de un editor de textos común se tratase.

.. code-block:: plain

  Alfred. Di "\n no funciona como un salto de línea,
  pero este mensaje va a ser multilínea. Además,
  si deseas tabular algo (\t), has de hacerlo      de esta manera".

**Resultado**:
  .. code-block::

    \n no funciona como un salto de línea,
    pero este mensaje va a ser multilínea. Además,
    si deseas tabular algo (\t), has de hacerlo      de esta manera

Escribe
-------

De la misma manera que la instrucción ``Di``, ``Escribe`` permite mostrar
textos por la salida estándar del sistema. La única diferencia es que no se
añade una salto de línea al evaluar la instrucción.

Esto es muy útil a la hora de concatenar textos.

.. code-block::

  Alfred. Escribe "Hola ", escribe "Mundo" y di "!".

**Resultado**:
  .. code-block::

    Hola Mundo!

Pregunta
--------

La instrucción ``Pregunta`` permite interactuar con la entrada estándar del
sistema. Esta instrucción hace uso de un parámetro **opcional**, el cual
corresponde al texto que va a ser mostrado antes de realizar la interacción con
el teclado.

.. code-block::

  Alfred. Pregunta.

.. code-block::

  Alfred,
  escribe "¿Cómo te llamas? " y pregunta.
  (es similar a...)
  Pregunta "¿Cómo te llamas? ".

.. WARNING::

  Es posible que en algunos sistemas, teclas como el tabulador, el retorno o las
  flechas no sean correctamente tratadas y den como resultado a entradas
  similares a ``^[[D`` o a ``^D``

El resultado es guardado en una variable especial propia de Alfred, llamada
**variable temporal**, la cual solamente es accesible mediante la instrucción
``Guardalo en``.

Guardalo en
-----------

La instrucción ``Guardalo en`` permite obtener el resultado de comandos tales
como ``Pregunta``, que hayan hecho uso de la **variable temporal**
característica de Alfred.

``Guardalo en`` toma como parámetro el nombre de la variable en la que se quiera
almacenar la información perteneciente a la **variable temporal**.

.. code-block::

  Alfred. Pregunta "¿Cómo te llamas? ", guardalo en nombre,
  escribe "Encantado de conocerte, " y di nombre.

**Resultado:**
  .. code-block:: plain

    ¿Como te llamas? Bruce
    Encantado de conocerte, Bruce
