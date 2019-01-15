module Main
where

--------

-- Alfred Modules
import Core.Source.Preprocessor     (process)
import Core.Environment.Argument    (runArgs)

--------

-- Entrypoint
main :: IO ()
main = do
    program <- runArgs
    print $ process program
    return ()