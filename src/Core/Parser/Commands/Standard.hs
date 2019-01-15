module Core.Parser.Commands.Standard
    (define'variable)
where

--------

-- Haskell Libraries
import Text.Parsec                              (space)
import Text.Parsec.String                       (Parser)

--------

-- Alfred Modules
import Core.Parser.Types                        (value,varname'd)
import Core.Language.Types                      (Command(DefineVariable))
import Core.Parser.Auxiliary                    (iC)
import Core.Language.Translations.ES as Lang    (define_variable)

--------

-- DefineVariable
-- -- define a variable
define'variable :: Parser Command
define'variable = do
    _ <- iC Lang.define_variable
    _ <- space
    n <- varname'd
    _ <- space
    v <- value
    return $ DefineVariable n v