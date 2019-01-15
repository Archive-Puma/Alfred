module Core.Environment.About
    (usage,check'version,show'version)
where

--------

-- Haskell Libraries
import Network.HTTP.Conduit         (simpleHttp)
import Data.ByteString.Lazy.Char8   (unpack)

--------

-- Dispay the help message
usage :: IO ()
usage = putStrLn "\n\
    \Alfred 2018 - Just another programming language...\n\
    \(c)2018 CosasDePuma.  All rights reserved.\n\
    \\n\
    \Usage:\n\
    \\talfred [-h] [-i] [-v] [--check-version] [filename.alf, ...]\n\
    \Options\n\
    \\t-h, --help\t\tDisplay this help message\n\
    \\t-i, --interactive\tRun Repl (interactive mode)\n\
    \\t    --check-version\tCheck if there is a newer version\n\
    \\t-v, --version\t\tDisplay version information and exit\n"

--------

-- Alfred's version
version :: String
version = "0.4.0"

-- Last Alfred's version (online)
last'version :: String
last'version = "https://raw.githubusercontent.com/CosasDePuma/Alfred/haskell/version.conf"

-- Display the version
show'version :: IO ()
show'version = putStrLn $ "alfred v" ++ version

-- Check if there is a new version
check'version :: IO ()
check'version = do
    response <- simpleHttp last'version
    let last = unpack response
    if version == last
        then putStrLn $ "Alfred is up to date."
        else putStrLn $ "There is a newer version: " ++ last