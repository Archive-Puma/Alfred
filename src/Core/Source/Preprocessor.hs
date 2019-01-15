module Core.Source.Preprocessor
    (process)
where

--------

-- Alfred Modules
import Core.Parser.Parser       (parse')
import Core.Language.Types      (Program)

--------

-- Remove blank lines from a text list
removeBlankLines :: [String] -> [String]
removeBlankLines xs = [ x | x <- xs, x /= "" ]

--------

-- Convert source code to AST
process :: String -> Program
process code = map parse' (removeBlankLines $ lines code)