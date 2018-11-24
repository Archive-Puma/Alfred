module Language where

--------

-- Aliases
type Name       = String
type Text       = String
type Character  = Char

--------

-- Data structure: Variables
data Variable =
  Number Integer
  | Text Text
  | Character Char
  deriving (Show)

-- Data structure: Special Tokens
data Token =
  CallAlfred
  | GoodbyeAlfred
  deriving(Show)

-- -- Data structure: Expressions
data Expression =
  Define Name Variable
  | Print Text
  | Show Name
  | ShowValue Name
  deriving(Show)
