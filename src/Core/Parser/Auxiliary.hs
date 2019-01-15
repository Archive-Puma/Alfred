module Core.Parser.Auxiliary
    (iC,format)
where

--------

-- Haskell Libraries
import Data.Char          (isSpace,toLower,toUpper)
import Text.Parsec        (char,choice,oneOf)
import Text.Parsec.String (Parser)

--------

-- Ignore the case of the given text
iC :: String -> Parser String
iC = mapM ignoreCase

-- Ignore the case of the given character
ignoreCase :: Char -> Parser Char
ignoreCase ch = choice [char (toLower ch), char (toUpper ch), oneOf "áéíóú", oneOf "ÁÉÍÓÚ"]

--------

-- Delete spaces at the beginning and end of the text
trim :: String -> String
trim = f . f where f = reverse . dropWhile isSpace

-- Format the given text
format :: String -> String
format = trim . map toLower