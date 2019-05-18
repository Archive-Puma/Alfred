===========
Instalación
===========

Alfred ha sido diseñado apoyándose en el lenguaje de programación **Python3**.
Es posible que en algunos Sistemas Operativos salten errores de dependencias incumplidas si Python no está instalado en el sistema.

Además, como Alfred aún está en fase de desarrollo, los archivos standalone y los módulos ejecutables no tienen ninguna garantía de
funcionar correctamente en cualquier sistema. En caso de encontrar una incompatibilidad, por favor, repórtala directamente en la `sección de errores del repositorio de GitHub`_.

.. _sección de errores del repositorio de GitHub: https://github.com/cosasdepuma/Alfred/issues


Linux
=====

Si estás corriendo Linux, tienes varias formas de conseguir a ``Alfred``.

La primera es descargar el `archivo standalone del repositorio de GitHub`_.
Aquí podrás encontrar todas las versiones junto a los cambios respecto a las anteriores versiones.
Una vez descagado, asegúrate de añadir la ruta del archivo a tu ``PATH`` o copiándolo en una ruta
que ya esté incluída.

.. _archivo standalone del repositorio de GitHub: https://github.com/cosasdepuma/Alfred/releases


También puedes instalar a ``Alfred`` mediante ``pip``. Asegúrate de tener instalado **Python3** junto a su
respectiva versión de **pip**:

.. code-block:: bash

  python --version
  pip --version

Una vez comprobado, sólamente tienes que ejecutar el siguiente comando:

.. code-block:: bash

  pip install alfred-lang
