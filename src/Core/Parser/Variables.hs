module Core.Parser.Variables (unquotedString, variable) where

--------

-- Haskell Libraries
import Text.Parsec              (between, char, digit, many, many1, noneOf, sepBy, try, parse, (<|>))
import Text.Parsec.String       (Parser)

--------

-- Alfred modules
import Lang.ES                  (lang_true, lang_false)
import Core.Language            (Variable (Booleano, Caracter, Lista, Numero, Texto))
import Core.Parser.Functions    (ignoreCase)

--------

true :: Parser Variable
true = do
  _ <- try (ignoreCase (lang_true !! 0)) <|> try (ignoreCase (lang_true !! 1)) <|> ignoreCase (lang_true !! 2)
  return (Booleano True)

false :: Parser Variable
false = do
  _ <- try (ignoreCase (lang_false !! 0)) <|> ignoreCase (lang_false !! 1)
  return (Booleano False)

--------

integer :: Parser Variable
integer = do
  neg <- (char '-' >> return '-') <|> return ' '
  num <- many1 digit
  return . Numero . read $ neg:num

--------

quotedChar :: Parser Variable
quotedChar = do
  quote <- try (char '\"') <|> char '\''
  ch    <- noneOf [quote]
  _     <- try (char quote)
  return (Caracter ch)

--------

quotedString :: Parser Variable
quotedString = do
  quote <- try (char '\"') <|> char '\''
  str   <- many (noneOf [quote])
  _     <- try (char quote)
  return (Texto str)

unquotedString :: Parser Variable
unquotedString = do
  str <- many1 (noneOf "\n")
  return (Texto str)

unquotedStringInList :: Parser Variable
unquotedStringInList = do
  str <- many1 (noneOf ",[]")
  return (Texto str)

--------

list :: Parser Variable
list = do
  content <- between (char '[') (char ']') (many (noneOf "]"))
  elems   <- case parse (sepBy (try variable <|> unquotedStringInList) (char ',')) "Alfred :: Parser :: List" content of
    Right elems'  -> return elems'
  return (Lista elems)

--------

variable :: Parser Variable
variable =  try true          <|>
            try false         <|>
            try integer       <|>
            try quotedChar    <|>
            try quotedString  <|>
                list
