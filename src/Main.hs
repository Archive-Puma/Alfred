module Main
where

--------

-- Alfred Modules
import Core.Source.Preprocessor     (process)
import Core.Source.Postprocessor    (evaluate)
import Core.Environment.Arguments   (runArgs)

--------

-- Entrypoint
main :: IO ()
main = do
    program <- runArgs
    let ast = process program
    evaluate ast
    return ()