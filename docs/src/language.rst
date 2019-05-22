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

.. code-block:: none

  [🐛] (Línea: 1) Sintaxis inválida: ...

De este modo, si se desea generar un programa ``.alf`` vacío, el contenido será
similar a este:

.. code-block:: none

  Alfred.

Comentarios
===========

Como casi cualquier otro lenguaje de programación, Alfred acepta la inclusión de
comentarios en el código. Aunque la semántica sea más que expresiva, en muchas
ocasiones es recomendable, por no decir necesario, el uso de anotaciones.

Para ello, se disponen de los símbolos ``(`` y ``)``, los cuales encapsularán
cualquier contenido que será ignorado a la hora de procesar el código.

.. code-block:: none

  (Los comentarios pueden ir precediendo a la palabra reservada Alfred)

  Alfred. (También pueden ir intercalados entre instrucciones) Di "Buenos días, Sr. Wayne".

  (Además, Alfred acepta comentarios
  multilínea sin la necesidad de
  caracteres especiales adicionales)

.. WARNING::

  Hay que tener cuidado al comentar código. La ausencia de un paréntesis puede
  convertir tus instrucciones en simples anotaciones.

.. code-block:: none

  Alfred.
  Di "Esto no es un comentario".
  (Hay que intentar no olvidarse de cerrar los comentarios
  Di "Esto es parte del comentario"
  (Alfred ignorará cualquier código si éste es tratado como un comentario)
  Di "Esto tampoco es parte de un comentario".

La ausencia de un paréntesis, es decir, si la cantidad total de pares de
paréntesis es impar, Alfred generará una excepción similar a esta:

.. code-block:: none

  [🐛] Caracter inválido (1,~184): (

Variables
=========

Lo que hace realmente versátiles a los lenguajes de programación es la
posibilidad de definir y trabajar con **variables**. Alfred no es una excepción
en este aspecto.

Para definir variables, existen varios métodos:

.. code-block:: none

  Alfred.
  (Define la variable X con el valor 10)
  X = 10.
  X es 10.
  X es igual a 10.

Todos ellos son funcionan de la misma manera, dándole el valor deseado a la
variable X.

Alfred reconoce automáticamente los diferentes tipos de variables y se encarga
de trabajar con ellos de la manera más adecuada. Actualmente se soportan estos
tipos de variables:

.. code-block:: none

  Alfred.
  (Tipo: Número Entero - No tiene decimales)
  Edad = 22.
  (Tipo: Texto - Ha de ir doblemente entrecomillado)
  Apellido = "Wayne".

Los nombres de variables desprecian el uso de mayúsulas y minúsculas, por lo que
``Àpellido``, ``APELLIDO``, ``apellido`` y ``ApeLLiDo`` tendrán el mismo valor.
Por otro lado, el nombre de las variables han de comenzar por una letra y sólo
está permitido el uso de letras, números y el símbolo ``_``.

Otra característica de las variables en Alfred, es que todas son mutables y
globales, pero esto es posible que cambie con la llegada de futuras versiones.

.. WARNING::

  Hay ciertas palabras, llamadas **palabras reservadas**, que no pueden ser
  usadas como identificadores para variables. Esas palabras son las siguientes,
  en cualquier combinación de mayúsculas y minúsculas:

  ``a``, ``alfred``, ``adios``, ``di``, ``en``, ``entre``, ``es``, ``escribe``,
  ``guardalo``, ``igual``, ``listo``, ``mas``, ``menos``, ``menor``, ``mayor``,
  ``mientras``, ``por``, ``pregunta``, ``que``, ``si``, ``sino``, ``y``

Instrucciones
=============

Di
--

La instrucción ``Di`` permite mostrar un texto por pantalla. Cualquier argumento
que se le pase será propiamente tratado para que se pueda mostrar por la salida
estándar del sistema. Además, un nuevo salto de línea será añadido tras evaluar
la instrucción.

.. code-block:: none

  Alfred. Di "Encantado de conocerte, Batman".

**Resultado**:
  .. code-block:: none

    Encantado de conocerte, Batman

.. ATTENTION::

  Los caracteres escapados tales como ``\n``, ``\r`` o ``\t`` **son tratados
  de manera literal**, por lo que si deseas que se muestren por pantalla,
  sólamente has de usarlos como si de un editor de textos común se tratase.

.. code-block:: none

  Alfred. Di "\n no funciona como un salto de línea,
  pero este mensaje va a ser multilínea. Además,
  si deseas tabular algo (\t), has de hacerlo      de esta manera".

**Resultado**:
  .. code-block:: none

    \n no funciona como un salto de línea,
    pero este mensaje va a ser multilínea. Además,
    si deseas tabular algo (\t), has de hacerlo      de esta manera

Escribe
-------

De la misma manera que la instrucción ``Di``, ``Escribe`` permite mostrar
textos por la salida estándar del sistema. La única diferencia es que no se
añade una salto de línea al evaluar la instrucción.

Esto es muy útil a la hora de concatenar textos.

.. code-block:: none

  Alfred. Escribe "Hola ", escribe "Mundo" y di "!".

**Resultado**:
  .. code-block:: none

    Hola Mundo!

Pregunta
--------

La instrucción ``Pregunta`` permite interactuar con la entrada estándar del
sistema. Esta instrucción hace uso de un parámetro **opcional**, el cual
corresponde al texto que va a ser mostrado antes de realizar la interacción con
el teclado.

.. code-block:: none

  Alfred. Pregunta.

.. code-block:: none

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

.. code-block:: none

  Alfred. Pregunta "¿Cómo te llamas? ", guardalo en nombre,
  escribe "Encantado de conocerte, " y di nombre.

**Resultado:**
  .. code-block:: none

    ¿Como te llamas? Bruce
    Encantado de conocerte, Bruce






Adios
-----

La instrucción ``Adiós`` es usada para detener de manera satisfactoria el flujo
del programa. Por ello, esta acción retornará **0** como código de salida.

.. code-block:: none

  Alfred. Adios.
