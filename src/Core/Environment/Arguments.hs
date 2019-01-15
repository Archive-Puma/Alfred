module Core.Environment.Arguments
    (runArgs)
where

--------

-- Haskell libraries
import System.Exit        (exitWith,ExitCode(ExitSuccess))
import System.Environment (getArgs)

--------

-- Alfred Modules
import Core.Environment.About   (usage,check'version,show'version)
--import Core.Repl          (runRepl)

--------

-- Exit the program successfully
exit :: IO a
exit = exitWith ExitSuccess

--------

-- Parse the arguments
parseArgs :: [String] -> IO String
-- -- run Repl
-- parseArgs [] = runRepl >> exit
-- parseArgs ["-i"] = runRepl >> exit
-- parseArgs ["--interactive"] = runRepl >> exit
-- -- display a help message
parseArgs ["-h"] = usage >> exit
parseArgs ["--help"] = usage >> exit
-- -- display the version of the program
parseArgs ["-v"] = show'version >> exit                     
parseArgs ["--version"] = show'version >> exit
-- -- check if there is a newer version                  
parseArgs ["--check-version"] = check'version >> exit
-- -- unhandled arguments
parseArgs [('-':_)] = usage >> exit
-- -- filenames
parseArgs filename = concat `fmap` mapM readFile filename

--------

-- Get and eval the arguments
runArgs :: IO String
runArgs = getArgs >>= parseArgs
