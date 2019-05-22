==========
Contribuir
==========

Si deseas contribuir en el desarrollo de Alfred, ¡no dudes en hacerlo!. Alfred
es un lenguaje de programación de código abierto y cualquier ayuda por parte de
la comunidad es bienvenida.

Herramientas necesarias
=======================

Para poder contribuir, es necesario tener algunas herramientas instaladas en el
sistema:

- `python3`_
- `pip3`_
- `git`_
- `make`_


Para disponer de un entorno controlado que no interfiera con el resto de tu
sistema, hay disponibles herramientas como `virtualenv`_ que puedes usar:

.. code-block:: powershell
  :caption: Windows

  pip install virtualenv

  virtualenv venv
  .\venv\Scripts\activate
  # ... comandos a ejecutar ...
  deactivate

.. code-block:: bash
  :caption: Linux

  pip install virtualenv

  virtualenv venv
  source venv/bin/activate
  # ... comandos a ejecutar ...
  deactivate

Obtener el Código Fuente
========================

Para descargar el código fuente de Alfred, puedes hacerlo mediante la utilidad
de `descarga directa`_ que ofrece GitHub. Aún así, es posible que luego tengas
que configurar el repositorio local para poder realizar **Pull Requets** (PR) o
mantenerlo actualizado.

Es por ello que la forma recomendable de obtener el código fuente es mediante
la herramienta de control de versiones ``git``:

.. code-block:: bash

  git clone https://github.com/CosasDePuma/Alfred

Para probar que la descarga se ha realizado con éxito, puedes poner el siguiente
comando dentro de la carpeta ``Alfred``:

.. code-block:: bash

  make check

Compilar el Código Fuente
=========================

Antes de compilar el programa, es necesario instalar los requisitos del código
fuente. Esto se realiza ejecutando los siguientes comandos:

.. code-block:: bash

  pip install -r requirements.txt
  pip install -r requirements-dev.txt

Alfred cuenta con varios archivos **Makefile** que proporcionan todas las
instrucciones necesarias, independientemente del Sistema Operativo que estés
usando. Para compilar, basta con escribir los comandos:

.. code-block:: bash

  make build
  make clean

Para instalar el módulo de manera local mediante ``pip``, basta con poner el
comando:

.. code-block:: bash

  make install

Esto sobreescrirá cualquier versión anterior que hayas instalado desde el
repositorio de ``PyPI``. De la misma manera, se puede desinstalar usando el
comando:

.. code-block:: bash

  make uninstall

.. WARNING::

  ``pip3`` ha de ser accesible de manera global mediante el comando ``pip`` para
  que las directivas ``install`` y ``uninstall`` funcionen correctamente.

.. Links
.. _python3: https://www.python.org/downloads/
.. _pip3: https://pypi.org/project/pip/
.. _git: https://git-scm.com/downloads
.. _make: https://www.gnu.org/software/make/
.. _virtualenv: https://pypi.org/project/virtualenv/
.. _descarga directa: https://github.com/CosasDePuma/Alfred/archive/master.zip
