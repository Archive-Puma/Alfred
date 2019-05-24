#!/usr/bin/python
# -*- coding: utf-8 -*-

# -- Imports -------------------------------------------------------------------

from argparse import ArgumentParser, SUPPRESS

# -- Version -------------------------------------------------------------------

try:
    with open("VERSION","r") as v:
        version = v.readline()
except FileNotFoundError:
    version = "Unknown"

# -- Argument Parser -----------------------------------------------------------

parser = ArgumentParser(
    description="Just another programming language...", add_help=False)

# -- Defaults ------------------------------------------------------------------

default = parser.add_argument_group("Opciones Elementales")
default.add_argument("-h", "--help", "--ayuda", action="help",
                default=SUPPRESS,
                help="Muestra este mensaje de ayuda y sale.")
default.add_argument("-v", "--version", action="version",
                version="%(prog)s {}".format(version),
                help="Muestra la versión del programa y sale.")

# -- Inputs --------------------------------------------------------------------

inputs = parser.add_argument_group("Métodos de Lectura")
inputs.add_argument("archivo", type=str, nargs="?", default=None,
                help="Archivo con el código fuente del programa.")
inputs.add_argument("-i", "--interactive", "--interactivo",
                action="store_true",
                help="Ejecuta el programa en modo interactivo.")

# -- Parser --------------------------------------------------------------------

argv = parser.parse_args()
argv.__parser__ = parser.parse_args
