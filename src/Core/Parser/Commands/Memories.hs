module Core.Parser.Commands.Memories
    (define'moment,goto')
where

--------

-- Haskell Libraries
import Text.Parsec                              (space)
import Text.Parsec.String                       (Parser)

--------

-- Alfred Modules
import Core.Parser.Types                        (f'text)
import Core.Language.Types                      (Command(DefineMoment,GotoMoment))
import Core.Parser.Auxiliary                    (iC)
import Core.Language.Translations.ES as Lang    (define_moment,goto)

--------

-- DefineMoment
-- -- define a moment (point to jump)
define'moment :: Parser Command
define'moment = do
    _ <- iC Lang.define_moment
    _ <- space
    n <- f'text
    return $ DefineMoment n

-- GotoMoment
-- -- jump to a moment
goto' :: Parser Command
goto' = do
    _ <- iC Lang.goto
    _ <- space
    n <- f'text
    return $ GotoMoment n