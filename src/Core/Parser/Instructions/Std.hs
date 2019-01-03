module Core.Parser.Instructions.Std (start',exit') where

--------

-- Haskell Libraries
import Text.Parsec            (char,many,many1)
import Text.Parsec.String     (Parser)

--------

-- Alfred modules
import Lang.ES                (lang_alfred,lang_bye)
import Core.Language          (Token(CallAlfred),Expression(Exit))
import Core.Parser.Functions  (ignoreCase)
import Core.Parser.Variables  (unquotedString,variable)

--------

-- Filter: Token - Alfred
start' :: Parser Token
start' = do
  _ <- ignoreCase lang_alfred
  _ <- many1 (char '\n')
  return CallAlfred

--------

-- Filter: Command - Adiós Alfred
exit' :: Parser Expression
exit' = do
  _ <- ignoreCase lang_bye
  _ <- many (char '\n')
  return Exit
