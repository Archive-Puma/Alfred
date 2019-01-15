module Core.Parser.Parser
    (parse')
where

--------

-- Haskell Libraries
import Text.Parsec (parse)

--------

-- Alfred Modules
import Core.Language.Types                      (Command(Error))
import Core.Parser.Commands                     (command)
import Core.Language.Translations.ES as Lang    (error_parse)

--------

-- Convert a command to a token
parse' :: String -> Command
parse' code =
    case parse command "" code of
        Right   value -> value
        Left    error -> Error (Lang.error_parse ++ ": " ++ code)