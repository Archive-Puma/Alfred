module Core.Interpreter (eval, evalRepl, runEval, memEmpty, Memory) where

--------

-- Haskell libraries
import qualified  Data.Map        as Map (size,empty, insert, lookup, Map)
import System.Exit

--------

-- Alfred modules
import            Core.Language

--------

-- Aliases
type Memory = Map.Map Nombre Variable

--------

parseJumps :: Monad m => Int -> Memory -> [Expression] -> m (Memory)
parseJumps _ jumps [] = return jumps
parseJumps ip jumps ((DefineLabel name):code) = parseJumps ip (Map.insert name (Numero ip) jumps) code
parseJumps ip jumps (_:code) = parseJumps (succ ip) jumps code

removeJumps :: Monad m => [Expression] -> [Expression] -> m [Expression]
removeJumps code []                     = return code
removeJumps code ((DefineLabel _):rest) = removeJumps code rest
removeJumps code (instruction:rest)     = removeJumps (code ++ [instruction]) rest

--------

-- Evaluation: No more lines of code
eval :: Memory
     -> Memory
     -> [String]
     -> [Expression]
     -> [Expression]
     -> IO (Map.Map Nombre Variable)
eval vars _ _ _ [] = return vars


-- Evaluation: Command - Vete/Salta a
eval vars jumps flags source ((Goto name):code) = case Map.lookup name jumps of
  Just ip -> case ip of
    Numero value -> eval vars jumps flags source $ drop value source
    otherwise    -> eval vars jumps flags source [Exit]
  Nothing -> eval vars jumps flags source [Exit]


-- Evaluation: Command - Define variable
eval vars jumps flags source ((DefineVar name value):code)   = do
  eval (Map.insert name value vars) jumps flags source code


-- Evaluation: Command - Escribe
eval vars jumps flags source ((Print text):code)             = do
  putStrLn text
  eval vars jumps flags source code


-- Evaluation: Command - Muestra
eval vars jumps flags source ((Show name):code)              = do
  case Map.lookup name vars of
    Just val -> print val
    Nothing -> putStrLn ""
  eval vars jumps flags source code


-- Evaluation: Command - Muestra el valor de
eval vars jumps flags source ((ShowValue name):code)         = do
  case Map.lookup name vars of
    Just variable -> case variable of
      Texto     val -> putStrLn val
      Numero    val -> putStrLn $ show val
      Caracter  val -> putStrLn [val]
    Nothing -> putStrLn ""
  eval vars jumps flags source code


-- Evaluation: Error
eval vars jumps flags source (Exit:code)                     = do
  exitWith ExitSuccess
  eval vars jumps flags source code


-- Evaluation: Error
eval vars jumps flags source (Error:code)                    = do
  putStrLn "Error :: Parser (Can't parse the code)"
  eval vars jumps flags source code


-- Evaluation: Error in Repl
eval vars jumps flags source ((ErrorRepl command):code)      = do
  putStrLn $ "Error :: Parser (Can't parse \"" ++ command ++ "\")"
  eval vars jumps flags source code


--------

-- Empty Memory
memEmpty :: Memory
memEmpty = Map.empty

-- Disable Jumps
disableJumps :: [String]
disableJumps = ["nojumps"]

--------

-- Evaluate a program
runEval :: [Expression] -> IO (Memory)
runEval code = do
  jumps <- parseJumps 0 memEmpty code
  code' <- removeJumps [] code
  eval memEmpty jumps [] code' code'

-- Evaluate REPL commands
evalRepl :: Memory -> [Expression] -> IO (Memory)
evalRepl memory code = eval memory memEmpty disableJumps [] code
