module Core.Language where

--------

-- Haskell Libraries
import Text.Parsec.Error

--------

-- Aliases
type Nombre    = String
type Texto     = String
type Caracter  = Char

--------

-- Data structure: Variables
data Variable =
  Numero Integer
  | Texto Texto
  | Caracter Caracter
  deriving (Show)

-- Data structure: Special Tokens
data Token =
  CallAlfred
  | GoodbyeAlfred
  deriving(Show)

-- -- Data structure: Expressions
data Expression =
  Define Nombre Variable
  | Print Texto
  | Show Nombre
  | ShowValue Nombre
  | Error
  | ErrorRepl String
  deriving(Show)
