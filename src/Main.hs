module Main where

--------

-- Alfred modules
import Parser       (runParser)
import Arguments    (runArgs)
import Interpreter  (runEval)

--------

-- Entrypoint
main :: IO ()
main = runArgs >>= runParser >>= runEval >> return ()
