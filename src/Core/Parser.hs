module Core.Parser where

--------

-- Haskell Libraries
import Data.Char          (isSpace, toLower, toUpper)
import Text.Parsec        (anyChar, char, digit, letter, many, many1, manyTill, oneOf, try, parse, (<|>))
import Text.Parsec.String (Parser)

--------

-- Alfred modules
import Lang.ES
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
  num <- many1 digit
  _   <- try (char '\n')
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
  _ <- ignoreCase lang_aldred
  _ <- char '\n'
  return CallAlfred


--------

-- Filter: Command - Adiós Alfred
exit' :: Parser Expression
exit' = do
  _ <- ignoreCase lang_bye
  _ <- try (char '\n')
  return Exit

define'label :: Parser Expression
define'label = do
  _     <- ignoreCase lang_moment
  _     <- char ' '
  name  <- manyTill anyChar (char '\n')
  return $ (DefineLabel . trim . map toLower) name

-- Filter: Command - Define
define'var :: Parser Expression
define'var = do
  _     <- ignoreCase lang_define
  _     <- char ' '
  name  <- manyTill (letter <|> char ' ') (try (ignoreCase lang_as))
  _     <- char ' '
  value <- try number <|> try character <|> text
  return $ (DefineVar . trim . map toLower) name value


goto' :: Parser Expression
goto' = do
  _     <- ignoreCase lang_go <|> ignoreCase lang_jump
  _     <- char ' '
  _     <- ignoreCase lang_to
  _     <- char ' '
  name  <- manyTill anyChar (char '\n')
  return $ (Goto . trim . map toLower) name


-- Filter: Command - Escribe
print' :: Parser Expression
print' = do
  _     <- ignoreCase lang_print
  _     <- char ' '
  text' <- manyTill anyChar (char '\n')
  return . Print $ text'

-- Filter: Command - Muestra
show' :: Parser Expression
show' = do
  _       <- ignoreCase lang_show
  _       <- char ' '
  onlyVal <- (try (ignoreCase lang_value) >> char ' ' >> return True) <|> return False
  name    <- manyTill anyChar (char '\n')
  return $ case onlyVal of
    True  -> (ShowValue . map toLower) name
    False -> (Show . map toLower) name

--------

-- Filter: All possible commands
command :: Parser Expression
command = try define'label  <|>
          try define'var    <|>
          try goto'         <|>
          try print'        <|>
          try show'         <|>
              exit'

-- Filter: Program struct
program :: Parser [Expression]
program = do
  _   <- start'
  ast <- many command
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
