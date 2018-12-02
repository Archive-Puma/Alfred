module Core.Parser.Instructions (command, program) where

--------

-- Haskell Libraries
import Data.Char              (toLower)
import Text.Parsec            (anyChar, char, letter, many, manyTill, try, (<|>))
import Text.Parsec.String     (Parser)

--------

-- Alfred modules
import Lang.ES
import Core.Language
import Core.Parser.Functions  (ignoreCase, trim)
import Core.Parser.Variables  (unquotedString, variable)

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

-- Filter: Command - Define momento
define'label :: Parser Expression
define'label = do
  _     <- ignoreCase lang_moment
  _     <- char ' '
  name  <- manyTill anyChar (char '\n')
  return $ (DefineLabel . trim . map toLower) name

-- Filter: Command - Define variable
define'var :: Parser Expression
define'var = do
  _     <- ignoreCase lang_define
  _     <- char ' '
  name  <- manyTill (letter <|> char ' ') (try (ignoreCase lang_as))
  _     <- char ' '
  value <- variable <|> unquotedString
  _     <- char '\n'
  return $ (DefineVar . trim . map toLower) name value


-- Filter: Command - Vete/Salta a
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
