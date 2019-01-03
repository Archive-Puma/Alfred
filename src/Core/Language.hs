module Core.Language where

--------

-- Aliases
type Nombre    = String

--------

-- Data structure: Variables
data Variable =
  Numero Int
  | Texto String
  | Booleano Bool
  | Caracter Char
  | Lista [Variable]
  deriving (Show, Eq)
instance Enum Variable where
  succ      (Numero value) = (Numero . succ) value
  toEnum    _ = undefined
  fromEnum  _ = undefined

-- Data structure: Special Tokens
data Token =
  CallAlfred
  deriving(Show)

-- -- Data structure: Expressions
data Expression =
  DefineLabel Nombre
  | DefineVar Nombre Variable
  | Goto Nombre
  | Print String
  | Show Nombre
  | ShowValue Nombre
  | Exit
  | Error
  | ErrorRepl String
  | Math Operation Nombre Variable
  deriving(Show)

data Operation =
  Add
  | Substract
  | Multiply
  deriving(Show)