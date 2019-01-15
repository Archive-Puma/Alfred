module Core.Language.Translations.ES
where

--------

space :: Char
space = ' '
-- Core
define,show' :: String
define  = "define"
show'   = "muestra"
-- Base
alfred,byalfred :: String
alfred      = "alfred"
byalfred    = "adios" ++ space : alfred
-- IO
write,show_type,show_value,show_variable :: String
write           = "escribe"
show_type       = show' ++ space : "el tipo de"
show_value      = show' ++ space : "el valor de"
show_variable   = show' ++ space : "la variable"
-- Memories
define_moment,goto :: String
goto            = "vete a"
define_moment   = define ++ space : "este momento como"
-- Standard
define_variable :: String
define_variable = define ++ space : "la variable"
-- Reserved words
reserved_as,reserved_equals :: String
reserved_as      = "como"
reserved_equals  = "igual a"
-- Errors
error_parse :: String
error_parse = "Error al analizar"