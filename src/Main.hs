module Main where

--------

-- Alfred modules
import Core.Parser       (runParser)
import Core.Arguments    (runArgs)
import Core.Interpreter  (runEval)

--------

-- Entrypoint
main :: IO ()
main = do
  runArgs >>= runParser >>= runEval >> return ()
