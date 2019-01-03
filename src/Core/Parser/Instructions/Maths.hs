module Core.Parser.Instructions.Maths (add'substract') where

    --------
    
    -- Haskell Libraries
    import Data.Char              (toLower)
    import Text.Parsec            (anyChar,char,digit,manyTill,try,(<|>))
    import Text.Parsec.String     (Parser)
    
    --------
    
    -- Alfred modules
    import Lang.ES                (lang_adds,lang_subs,lang_to)
    import Core.Language          (Expression(Math),Operation(Add,Substract))
    import Core.Parser.Functions  (ignoreCase,trim)
    import Core.Parser.Variables  (integer)
    
    --------
    
    -- Filter: Command - Súmale / Réstale
    add'substract' :: Parser Expression
    add'substract' = do
      command   <- try adds <|> subs
      _         <- char ' '
      quantity  <- integer
      _         <- char ' '
      _         <- ignoreCase lang_to
      name      <- manyTill anyChar (char '\n')
      return $ Math command ((trim . map toLower) name) quantity
    
    --------
    
    -- Filter: Operation - Addition
    adds :: Parser Operation
    adds = ignoreCase lang_adds >> return Add

    -- Filter: Operation - Substraction
    subs :: Parser Operation
    subs = ignoreCase lang_subs >> return Substract