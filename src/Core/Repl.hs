module Core.Repl (runRepl) where

--------

-- Haskell libraries
import System.IO   (stdout, hFlush)

--------

-- Alfred Modules
import Core.Parser      (parseRepl)
import Core.Interpreter (evalRepl, memEmpty, Memory)

--------

-- Display the welcome message
header :: IO ()
header = do
  putStrLn "Alfred 2018 - Just another programming language..."
  putStrLn "(c)2018 CosasDePuma.  All rights reserved."
  putStrLn "Interactive mode. Press Ctrl + C to quit."
  putStrLn ""

-- Infinite loop (Read Eval Print Loop)
interactiveMode :: Memory -> IO b
interactiveMode memory = do
  putStr "🎩 ~ "
  hFlush stdout
  ast <- getLine >>= parseRepl
  print ast
  evalRepl memory ast >>= interactiveMode

-- Show the message and run the Repl
runRepl :: IO b
runRepl = do
  header
  interactiveMode memEmpty
