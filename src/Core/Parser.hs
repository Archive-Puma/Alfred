module Core.Parser where

--------

-- Haskell Libraries
import Data.Char          (isSpace, toLower, toUpper)
import Text.Parsec        (anyChar, char, digit, letter, many, manyTill, oneOf, try, parse, (<|>))
import Text.Parsec.String (Parser)

--------

-- Alfred modules
import Core.Language

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

--------

-- Filter: Numero as a Variable Value
number :: Parser Variable
number = do
  num <- manyTill digit (char '\n')
  return . Numero . read $ num

-- Filter: Text as a Variable Value
text :: Parser Variable
text = do
  txt <- manyTill anyChar (char '\n')
  return . Texto $ txt

-- Filter: Caracter as a Variable Value
character :: Parser Variable
character = do
  ch  <- anyChar
  _   <- char '\n'
  return . Caracter $ ch

--------

-- Filter: Token - Alfred
start' :: Parser Token
start' = do
  _ <- ignoreCase "alfred"
  _ <- char '\n'
  return CallAlfred

-- Filter: Token - Adiós Alfred
end' :: Parser Token
end' = do
  _ <- ignoreCase "adios alfred"
  return GoodbyeAlfred

--------

-- Filter: Command - Define
define' :: Parser Expression
define' = do
  _     <- ignoreCase "define"
  _     <- char ' '
  name  <- manyTill (letter <|> char ' ') (try (ignoreCase "como"))
  _     <- char ' '
  value <- try number <|> try character <|> text
  let name' = (trim . map toLower) name
  return $ Define name' value

-- Filter: Command - Escribe
print' :: Parser Expression
print' = do
  _     <- ignoreCase "escribe"
  _     <- char ' '
  text' <- manyTill anyChar (char '\n')
  return . Print $ text'

-- Filter: Command - Muestra
show' :: Parser Expression
show' = do
  _       <- ignoreCase "muestra"
  _       <- char ' '
  onlyVal <- (try (ignoreCase "el valor de") >> char ' ' >> return True) <|> return False
  name    <- manyTill anyChar (char '\n')
  let name' = map toLower name
  return $ case onlyVal of
    True  -> ShowValue name'
    False -> Show name'

--------

-- Filter: All possible commands
command :: Parser Expression
command =  try define' <|>
           try print'  <|>
               show'

-- Filter: Program struct
program :: Parser [Expression]
program = do
  _   <- start'
  ast <- many command
  _   <- end'
  return ast

--------

-- Parse single commands (Repl)
parseRepl :: Monad m => String -> m [Expression]
parseRepl src = case parse command "Alfred :: Repl" (src ++ "\n") of
  Right ast -> return [ast]
  Left  _   -> return [ErrorRepl src]

-- Parse programs
runParser :: Monad m => String -> m [Expression]
runParser src = case parse program "Alfred :: Parser" src of
  Right ast -> return ast
  Left  _   -> return [Error]
