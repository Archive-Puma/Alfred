.. Reference: https://golang.org/doc/install

===========
Instalación
===========

Alfred ha sido diseñado apoyándose en el lenguaje de programación **Python3**.
Es posible que en algunos Sistemas Operativos salten errores de dependencias
incumplidas si Python no está instalado en el sistema.

Además, como Alfred aún está en fase de desarrollo, los archivos standalone y
los módulos ejecutables no tienen ninguna garantía de funcionar correctamente
en cualquier sistema. En caso de encontrar una incompatibilidad, puedes
reportarla directamente en la `sección de errores del repositorio de GitHub`_.

Linux
=====

Si estás corriendo Linux, tienes varias formas de conseguir a ``Alfred``.

La primera es `descargar el archivo` correspondiente a tu distribución y
arquitectura desde `repositorio de GitHub`_. Aquí podrás encontrar todas las
versiones junto a los cambios realizados respecto a las anteriores versiones.

Una vez descagado, asegúrate de añadir la ruta del archivo a tu ``PATH``.
Para ello puedes crear una nueva ruta en la que poner tu binario, por ejemplo
``/usr/local/alfred/bin``. Para poder acceder a él desde cualquier parte de tu
terminal, puedes añadir la siguiente línea al archivo ``$HOME/.profile`` o al
archivo ``/etc/profile`` (en caso de que desees una instalación para todos los
usuarios del sistema):

.. code-block:: bash

  export PATH=$PATH:/usr/local/alfred/bin

También puedes instalar a ``Alfred`` mediante ``pip``. Asegúrate de tener
instalado **Python3** junto a su correspondiente versión de **pip**:

.. code-block:: bash

  python --version
  pip --version

Una vez comprobado, sólamente tienes que ejecutar el siguiente comando:

.. code-block:: bash

  pip install alfred-lang

Probando la instalación
=======================

Desde tu terminal, prueba a poner el siguiente comando:

.. code-block: bash

  alfred

Si te aparece el mensaje de ayuda, significa que la instalación se ha realizado
con éxito.

Puedes probar tus habilidades con este lenguaje de programación mediante el modo
interactivo o ejecutando tus programas:

.. code-block:: bash

  alfred -i
  alfred --interactive

  alfred holamundo.alf

.. Links
.. _repositorio de GitHub: https://github.com/cosasdepuma/Alfred
.. _descargar el archivo: https://github.com/cosasdepuma/Alfred/releases
.. _sección de errores del repositorio de GitHub: https://github.com/cosasdepuma/Alfred/issues
