module Core.Parser.Commands.Base
    (alfred',bye'alfred,comment')
where

--------

-- Haskell Libraries
import Text.Parsec                              (between,char,many,noneOf)
import Text.Parsec.String                       (Parser)

--------

-- Alfred Modules
import Core.Language.Types                      (Command(HiAlfred,ByeAlfred,Comment))
import Core.Parser.Auxiliary                    (iC)
import Core.Language.Translations.ES as Lang    (alfred,byalfred)

--------

-- HiAlfred
-- -- init the program (needed entrypoint)
alfred' :: Parser Command
alfred' = iC Lang.alfred >> return HiAlfred

--------

-- ByeAlfred
-- -- stop the program
bye'alfred :: Parser Command
bye'alfred = iC Lang.byalfred >> return ByeAlfred

--------

-- Comment
-- -- ignore this lines
comment' :: Parser Command
comment' = between (char '(') (char ')') (many $ noneOf ")") >> return Comment