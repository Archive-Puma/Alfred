module Core.Language.Types
where

--------

type Msg        = String
type Name       = String
type Program    = [Command]

--------

data Value =
    Texto String
    | Booleano Bool
    | Entero Int
    deriving (Eq,Show)

--------

data Command = 
    -- Base
    HiAlfred
    | ByeAlfred
    -- Standard
    | DefineVariable Name Value
    -- Memories
    | DefineMoment Name
    | GotoMoment Name
    -- IO
    | Write Msg
    | ShowType Name
    | ShowValue Name
    | ShowVariable Name
    -- Other
    | Error Msg
    deriving (Eq,Show)