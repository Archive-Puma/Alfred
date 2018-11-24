module Main where

--------

-- Alfred modules
import            Alfred.Parser       (runParser)
import            Alfred.Arguments    (runArgs)
import            Alfred.Interpreter  (runEval)

--------

-- Entrypoint
main :: IO ()
main = runArgs >>= runParser >>= runEval >> return ()
