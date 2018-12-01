module Core.Language where

--------

-- Aliases
type Nombre    = String
type Texto     = String
type Caracter  = Char

--------

-- Data structure: Variables
data Variable =
  Numero Int
  | Texto Texto
  | Caracter Caracter
  deriving (Show, Eq)
instance Enum Variable where
  succ      (Numero value) = (Numero . succ) value
  toEnum    _ = undefined
  fromEnum  _ = undefined

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
