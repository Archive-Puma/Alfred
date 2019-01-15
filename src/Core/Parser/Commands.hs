module Core.Parser.Commands
    (command)
where

--------

-- Haskell Libraries
import Text.Parsec                      (try,(<|>))
import Text.Parsec.String               (Parser)

--------

-- Alfred Modules
import Core.Language.Types              (Command)

import Core.Parser.Commands.Base        (alfred',bye'alfred)
import Core.Parser.Commands.IO          (write',show'type,show'value,show'variable)
import Core.Parser.Commands.Memories    (define'moment,goto')
import Core.Parser.Commands.Standard    (define'variable)

--------

-- List of available commands
command :: Parser Command
command =   try alfred'         <|>
            try bye'alfred      <|>
            try define'moment   <|>
            try define'variable <|>
            try goto'           <|>
            try show'type       <|>
            try show'value      <|>
            try show'variable   <|>
                write'
