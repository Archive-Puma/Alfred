module Core.Parser.Types
    (f'text,text,value,varname'd)
where

--------

-- Haskell Libraries
import Text.Parsec                              (alphaNum,anyChar,char,choice,digit,letter,
                                                many1,manyTill,optionMaybe,space,try,(<|>))
import Text.Parsec.String                       (Parser)

--------

-- Alfred Modules
import Core.Language.Types                      (Value(Entero,Texto))
import Core.Parser.Auxiliary                    (iC,format)
import Core.Language.Translations.ES as Lang    (reserved_as,reserved_equals)

--------

-- All characters to the end
text :: Parser String
text = many1 anyChar

-- All characters to the end formatted
f'text :: Parser String
f'text = do
    t <- text
    return $ format t


--------

-- A valid variable value
value :: Parser Value
value = choice [integer,unquoted]

--------

-- A valid variable name (define command)
varname'd :: Parser String
varname'd = do
    h <- letter
    t <- optionMaybe $ manyTill validchars reserved'define
    return $ case t of
        Just r  -> format (h:r)
        Nothing -> "ERROR" -- FIXME

--------

-- Valid characters in a variable name
validchars :: Parser Char
validchars =    try alphaNum  <|>
                    space

-- Reserved words in a define command
reserved'define :: Parser String
reserved'define = choice [iC reserved_as, iC reserved_equals]

--------

{- VALID TYPES OF VARIABLES -}

-- Integers
integer :: Parser Value
integer = do
    m <- (char '-' >> return '-') <|> return ' '
    n <- many1 digit
    return . Entero . read $ m:n

-- Unquoted texts
unquoted :: Parser Value
unquoted = do
    t <- text
    return . Texto $ t