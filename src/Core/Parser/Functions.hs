module Core.Parser.Functions (ignoreCase, trim) where

--------

-- Haskell Libraries
import Data.Char          (isSpace, toLower, toUpper)
import Text.Parsec        (char, oneOf, (<|>))
import Text.Parsec.String (Parser)

--------

-- Remove initial and final blank spaces
trim :: String -> String
trim = f . f where f = reverse . dropWhile isSpace

-- Parse upper and lower chars as the same char
insensitiveChar :: Char -> Parser Char
insensitiveChar ch = char (toLower ch) <|> char (toUpper ch) <|> (oneOf "áéíóú") <|> (oneOf "ÁÉÍÓÚ")

-- Parse strings ignoring case
ignoreCase :: String -> Parser String
ignoreCase = mapM insensitiveChar
