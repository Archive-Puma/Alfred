module Core.Parser where

--------

-- Haskell Libraries
import Text.Parsec (parse)

--------

-- Alfred Modules
import Core.Language
import Core.Parser.Instructions (command, program)

--------

-- Parse single commands (Repl)
parseRepl :: Monad m => String -> m [Expression]
parseRepl src = case parse command "Alfred :: Repl" (src ++ "\n") of
  Right ast -> return [ast]
  Left  _   -> return [ErrorRepl src]

-- Parse programs
runParser :: Monad m => String -> m [Expression]
runParser src = case parse program "Alfred :: Parser" src of
  Right ast -> return ast
  Left  _   -> return [Error]
