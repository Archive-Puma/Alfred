<h1 align="center">
	<img
		width="300"
		alt="Alfred Haskell"
		src="./.repo/alfred.png">
</h1>
<h1 align="center">
	<strong>
    Alfred
  </strong>
</h1>
<p align="center">
	<strong>
    Just another programming language
	</strong>
</p>
<p align="center">
  <a href="https://circleci.com/gh/CosasDePuma/Alfred/tree/python3">
    <img
      alt="Build"
      src="https://img.shields.io/circleci/project/github/CosasDePuma/Alfred/python3.svg?style=flat-square&logo=circleci">
  </a>

  <a href="https://github.com/CosasDePuma/Alfred/tree/python3">
    <img
      alt="Version"
      src="https://img.shields.io/badge/version-v0.5.5-blue.svg?style=flat-square">
  </a>
</p>




:vhs: Clone the repository!
----
Clone or download the project:
```sh
git clone https://github.com/cosasdepuma/alfred.git --branch python3 Alfred-Python3
```




:wrench: Build the interpreter
---
All the compiled files will be placed in the `dist` directory.


You can compile the interpreter running the following command

```sh
make
```
>  :warning: This option is not available for Windows devices.

>  :warning: The `make` program must be installed on the system.

Before compiling the interpreter, it is necessary to check and correct the requirements with the command:

```bash
python3     --version
pip3        --version
virtualenv  --version

virtualenv build-env

# Windows
.\build-env\bin\activate.ps1
# Linux
source build-env/bin/activate

# Inside the virtual environment
pip3 install --upgrade pyinstaller
```

If `make` is not available, PyInstaller can be executed using the following command:

```bash
pyinstaller --onefile --noconfirm --clean --log-level=WARN src/main.py
```

:books: Docs
---
You can find a complete documentation in this [Wiki](https://github.com/cosasdepuma/alfred/wiki).


:octopus: Support the developer!
----
Everything I do and publish can be used for free whenever I receive my corresponding merit.

Anyway, if you want to help me in a more direct way, you can leave me a tip by clicking on this badge:

<p align="center">
    </br>
    <a href="https://www.paypal.me/cosasdepuma/"><img src="https://img.shields.io/badge/Donate-PayPal-blue.svg?style=for-the-badge&logo=paypal" alt="PayPal Donation"></img></a>
</p>




:earth_africa: Scheme of contents
----
```
Alfred (Python3)
 < Repository >
|__ .repo
| |__ alfred.png
|__ .gitignore
|__ LICENSE
|__ README.md
|__ CHANGELOG
< Build >
|__ Makefile
|__ requirements.txt
< CD/CI >
|__ .circleci
| |__ config.yml
< Distribution >
|__ dist
| |__ alfred-v0.5.5.elf
< Source >
|__ src
| |__ Core
| | |__ Environment
| | | |__ __init__.py
| | | |__ Arguments.py
| | |__ Evaluator
| | | |__ Commands
| | | | |__ Control
| | | | | |__ __init__.py
| | | | | |__ Moments.py
| | | | |__ IO
| | | | | |__ __init__.py
| | | | | |__ Base.py
| | | | | |__ Show.py
| | | | |__ Network
| | | | | |__ __init__.py
| | | | | |__ HTTP.py
| | | | |__ __init__.py
| | | | |__ Base.py
| | | | |__ Math.py
| | | | |__ Standard.py
| | | |__ __init__.py
| | | |__ Base.py
| | |__ Language
| | | |__ Translations
| | | | |__ __init__.py
| | | | |__ ES.py
| | | |__ __init__.py
| | | |__ Binds.py
| | |__ Parser
| | | |__ __init__.py
| | | |__ Base.py
| | |__ Source
| | | |__ __init__.py
| | | |__ Preprocessor.py
| | |__ __init__.py
| |__ main.py
< Alfred Examples >
|_ examples
  |_ 00.Pruebas.alf
  |_ 01.HolaBatman.alf
  |_ 02.Variables.alf
  |_ 03.Momentos.alf
	|_ 04.Matemáticas.alf
  |_ 05.ServidoresHTTP.alf
```
