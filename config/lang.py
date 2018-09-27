"""
Author: @CosasDePuma <kikefontanlorenzo@gmail.com>(https://github.com/cosasdepuma)
"""

from importlib import import_module

def manager(lang):
    """ Manager to import the custom language support """
    keywords = import_module('config.support.' + lang.lower()).KEYWORDS
    controlflow_keywords = import_module('config.support.' + lang.lower()).CONTROLFLOW_KEYWORDS
    return keywords, controlflow_keywords
