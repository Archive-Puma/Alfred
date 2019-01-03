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
  <a href="https://circleci.com/gh/CosasDePuma/Alfred/tree/haskell">
    <img
      alt="Build"
      src="https://img.shields.io/circleci/project/github/CosasDePuma/Alfred/haskell.svg?style=flat-square&logo=circleci">
  </a>

  <a href="https://github.com/CosasDePuma/Alfred/tree/haskell">
    <img
      alt="Version"
      src="https://img.shields.io/badge/version-v0.3.0-blue.svg?style=flat-square">
  </a>
</p>




:vhs: Clone the repository!
----
Clone or download the project:
```sh
git clone https://github.com/cosasdepuma/alfred.git --branch haskell Alfred-Haskell
```




:wrench: Build the interpreter
---
All the compiled files will be placed in the `dist` directory.


You can compile the interpreter in two different ways but both are totally valid:

### Makefile

>  :warning: This option is not available for Windows devices.

>  :warning: The `make` program must be installed on the system.

Before compiling the interpreter, it is necessary to check and correct the requirements with the command:

```bash
make configure
```

Now we can start the process running:

```bash
make build
```

Finally, we will delete all the unwanted files from the compilation process:

```bash
make clean
```

The compilation process can be reduced to a single command:

```bash
make
```

### Cabal

You can compile the interpreter using `cabal` simply with the command:

```bash
cabal build
```




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
Alfred (Haskell)
 < Repository >
|__ .repo
|	|__ alfred.png
|__ .gitignore
|__ LICENSE
|__ README.md
< Build >
|__ Makefile
|__ Setup.hs
|__ alfred.cabal
< CD/CI >
|__ .circleci
|	|__ config.yml
< Distribution >
|__ dist
|	|__ build
|	 	|__ alfred
|	 	|	|__ alfred
|	 	|__ alfred-test
|	 		|__ alfred-test
< Source >
|__ src
|	|__ Main.hs
|	|__ Core
|	|	|__ Parser
|	|	|	|__ Instructions
|	|	|	|	|__ Jumps.hs
| | | | |__ Maths.hs
|	|	|	|	|__ Std.hs
|	|	|	|	|__ Stdout.hs
|	|	|	|	|__ Variables.hs
|	|	|	|__ Functions.hs
|	|	|	|__ Instructions.hs
|	|	|	|__ Stdout.hs
|	|	|	|__ Variables.hs
|	|	|_ Arguments.hs
|	|	|_ Interpreter.hs
|	|	|_ Parser.hs
|	|	|_ Repl.hs
< Language Support >
|	|_ Lang
|	 	|_ ES.hs
< Unit Test >
|_ test
|	|_ Parser
|	|	|_ FunctionsSpecs.hs
|	|_ Main.hs
|	|_ Spec.hs
< Alfred Examples >
|_ example
	|_ holamundo.alf
	|_ momentos_inversos.alf
	|_ momentos.alf
	|_ variables.alf
```
