module Core.Parser.Instructions.Stdout (print',show',show'value) where

--------

-- Haskell Libraries
import Data.Char              (toLower)
import Text.Parsec            (anyChar,char,manyTill,try,(<|>))
import Text.Parsec.String     (Parser)

--------

-- Alfred modules
import Lang.ES                (lang_print,lang_show,lang_value)
import Core.Language          (Expression(Print,Show,ShowValue))
import Core.Parser.Functions  (ignoreCase)

--------

-- Filter: Command - Escribe
print' :: Parser Expression
print' = do
  _     <- ignoreCase lang_print
  _     <- char ' '
  text' <- manyTill anyChar (char '\n')
  (return . Print) text'

--------

-- Filter: Command - Muestra
show' :: Parser Expression
show' = do
  _     <- ignoreCase lang_show
  _     <- char ' '
  name  <- manyTill anyChar (char '\n')
  (return . Show . map toLower) name

-- Filter: Command - Muestra el valor de
show'value :: Parser Expression
show'value = do
  _     <- ignoreCase lang_show
  _     <- char ' '
  _     <- ignoreCase lang_value
  _     <- char ' '
  name  <- manyTill anyChar (char '\n')
  (return . ShowValue . map toLower) name
