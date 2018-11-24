module Main where

--------

-- Haskell modules
import qualified  Data.Map    as Map  (empty)
import            Text.Parsec         (parse)

--------

-- Alfred modules
import            Alfred.Parser       (runParser)
import            Alfred.Arguments    (runArgs)
import            Alfred.Interpreter  (runEval)

--------

-- Entrypoint
main :: IO ()
main = runArgs >>= runParser >>= runEval >> return ()
