module Core.Source.Postprocessor
    (evaluate)
where

--------

-- Alfred Modules
import Core.Language.Types  (Program,Command(HiAlfred,Comment))

--------

-- Remove comments from AST
uncomment :: Program -> Program
uncomment program = [ x | x <- program, x /= Comment ]

--------

-- Check the initial command
evaluate :: Program -> IO ()
evaluate program = do
    let code = uncomment program
    case head code of
        HiAlfred  -> evaluate' $ tail code
        otherwise -> putStrLn "Error" -- FIXME

-- Run the commands
evaluate' :: Program -> IO ()
evaluate' [] = return ()
evaluate' (command:program) = print command >> evaluate' program
