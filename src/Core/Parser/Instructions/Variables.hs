module Core.Parser.Instructions.Variables (define'var) where

--------

-- Haskell Libraries
import Data.Char              (toLower)
import Text.Parsec            (char,letter,manyTill,try,(<|>))
import Text.Parsec.String     (Parser)

--------

-- Alfred modules
import Lang.ES                (lang_as,lang_define)
import Core.Language          (Expression(DefineVar))
import Core.Parser.Functions  (ignoreCase,trim)
import Core.Parser.Variables  (unquotedString,variable)

--------

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
