module Core.Parser.Instructions (command,program) where

--------

-- Haskell Libraries
import Text.Parsec                         (char,many,try,(<|>))
import Text.Parsec.String                  (Parser)

--------

-- Alfred modules
import Lang.ES
import Core.Language
import Core.Parser.Functions              (ignoreCase,trim)
import Core.Parser.Variables              (unquotedString,variable)
import Core.Parser.Instructions.Std       (start',exit')
import Core.Parser.Instructions.Jumps     (define'label,goto')
import Core.Parser.Instructions.Maths     (add'substract')
import Core.Parser.Instructions.Stdout    (print',show',show'value)
import Core.Parser.Instructions.Variables (define'var)

--------

-- Filter: All possible commands
command :: Parser Expression
command = try define'label    <|>
          try define'var      <|>
          try goto'           <|>
          try print'          <|>
          try show'value      <|>
          try show'           <|>
          try add'substract'  <|>
              exit'

--------

-- Filter: Program struct
program :: Parser [Expression]
program = do
  _   <- start'
  ast <- many command
  return ast
