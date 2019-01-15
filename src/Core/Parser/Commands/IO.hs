module Core.Parser.Commands.IO
    (write',show'type,show'value,show'variable)
where

--------

-- Haskell Libraries
import Text.Parsec                              (space)
import Text.Parsec.String                       (Parser)

--------

-- Alfred Modules
import Core.Parser.Types                        (f'text,text)
import Core.Language.Types                      (Command(Write,ShowType,ShowValue,ShowVariable))
import Core.Parser.Auxiliary                    (iC)
import Core.Language.Translations.ES as Lang    (write,show_type,show_value,show_variable)

--------

-- Write
-- -- write a text in the stdout
write' :: Parser Command
write' = do
    _ <- iC Lang.write
    _ <- space
    t <- text
    return $ Write t

--------

-- ShowType
-- -- write the type of a variable
show'type :: Parser Command
show'type = do
    _ <- iC Lang.show_type
    _ <- space
    n <- f'text
    return $ ShowType n

-- ShowValue
-- -- write the content of a variable
show'value :: Parser Command
show'value = do
    _ <- iC Lang.show_value
    _ <- space
    n <- f'text
    return $ ShowValue n

-- ShowVariable
-- -- write the type and content of a variable
show'variable :: Parser Command
show'variable = do
    _ <- iC Lang.show_variable
    _ <- space
    n <- f'text
    return $ ShowVariable n
