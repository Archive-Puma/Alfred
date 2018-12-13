module Core.Parser.Instructions.Jumps (define'label,goto') where

--------

-- Haskell Libraries
import Data.Char              (toLower)
import Text.Parsec            (anyChar,char,manyTill,(<|>))
import Text.Parsec.String     (Parser)

--------

-- Alfred modules
import Lang.ES                (lang_go,lang_jump,lang_moment,lang_to)
import Core.Language          (Expression(DefineLabel,Goto))
import Core.Parser.Functions  (ignoreCase,trim)

--------

-- Filter: Command - Define momento
define'label :: Parser Expression
define'label = do
  _     <- ignoreCase lang_moment
  _     <- char ' '
  name  <- manyTill anyChar (char '\n')
  return $ (DefineLabel . trim . map toLower) name

--------

-- Filter: Command - Vete/Salta a
goto' :: Parser Expression
goto' = do
  _     <- ignoreCase lang_go <|> ignoreCase lang_jump
  _     <- char ' '
  _     <- ignoreCase lang_to
  _     <- char ' '
  name  <- manyTill anyChar (char '\n')
  return $ (Goto . trim . map toLower) name
