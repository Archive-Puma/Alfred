module Interpreter (eval, runEval, memEmpty, Memory) where

--------

-- Haskell libraries
import qualified  Data.Map        as Map (empty, insert, toList, lookup, Map)

--------

-- Alfred modules
import            Language

--------

-- Aliases
type Memory = Map.Map Nombre Variable

--------

-- Evaluation: No more lines of code
eval :: Memory -> [Expression] -> IO (Memory)
eval vars [] = return vars
-- Evaluation: Command - Define
eval vars ((Define name value):code) =
  eval (Map.insert name value vars) code
-- Evaluation: Command - Escribe
eval vars ((Print text):code) = do
  putStrLn text
  eval vars code
-- Evaluation: Command - Muestra
eval vars ((Show name):code) = do
  case Map.lookup name vars of
    Just val -> print val
    Nothing -> putStrLn ""
  eval vars code
-- Evaluation: Command - Muestra el valor de
eval vars ((ShowValue name):code) = do
  case Map.lookup name vars of
    Just variable -> case variable of
      Texto     val -> putStrLn val
      Numero    val -> putStrLn $ show val
      Caracter  val -> putStrLn [val]
    Nothing -> putStrLn ""
  eval vars code

--------

-- Empty Memory
memEmpty :: Memory
memEmpty = Map.empty

-- Evaluate a program
runEval :: [Expression] -> IO (Memory)
runEval = eval Map.empty
