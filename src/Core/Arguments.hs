module Core.Arguments (runArgs) where

--------

-- Haskell libraries
import System.Exit        (exitWith, ExitCode(ExitSuccess))
import System.Environment (getArgs)

--------

-- Alfred Modules
import Core.Repl               (runRepl)

--------

-- Dispay the help message
usage :: IO ()
usage = putStrLn "\n\
  \Alfred 2018 - Just another programming language...\n\
  \(c)2018 CosasDePuma.  All rights reserved.\n\
  \\n\
  \Usage:\n\
  \\talfred [-h] [-i] [-v] [filename.alf, ...]\n\
  \Options\n\
  \\t-h, --help\t\tDisplay this help message\n\
  \\t-i, --interactive\tRun Repl (interactive mode)\n\
  \\t-v, --version\t\tDisplay version information and exit\n"

-- Display the version
version :: IO ()
version = putStrLn "alfred v0.3.0 ~ py2hs"

-- Exit the program successfully
exit :: IO a
exit = exitWith ExitSuccess

-- Parse the arguments
parseArgs :: [String] -> IO String
parseArgs [] = runRepl >> exit                            -- Run Repl
parseArgs ["-i"] = runRepl >> exit
parseArgs ["--interactive"] = runRepl >> exit
parseArgs ["-h"] = usage >> exit                          -- Display a help message
parseArgs ["--help"] = usage >> exit
parseArgs ["-v"] = version >> exit                        -- Display the version of the program
parseArgs ["--version"] = version >> exit
parseArgs [('-':_)] = usage >> exit                       -- Display a help message
parseArgs filename = concat `fmap` mapM readFile filename -- Concatenate all the source files

-- Get and eval the arguments
runArgs :: IO String
runArgs = getArgs >>= parseArgs
