module Core.Language where

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
  deriving (Show, Eq)

-- Data structure: Special Tokens
data Token =
  CallAlfred
  | GoodbyeAlfred
  deriving(Show)

-- -- Data structure: Expressions
data Expression =
  DefineLabel Nombre
  | DefineVar Nombre Variable
  | Print Texto
  | Show Nombre
  | ShowValue Nombre
  | Goto Nombre
  | Exit
  | Error
  | ErrorRepl String
  deriving(Show)
