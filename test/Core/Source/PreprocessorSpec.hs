module Core.Source.PreprocessorSpec where

--------

-- Haskell Libraries
import Test.Hspec                       (describe,it,shouldBe,SpecWith)

--------

-- Alfred Modules
import Core.Source.Preprocessor

import Core.Language.Types

--------

-- Entrypoint
spec :: SpecWith ()
spec = do
    ----
    describe "process :: Convert source code to AST" $ do

        {- BASE -} 
        
        it "[aaa] HiAlfred" $ do
            process "alfred" `shouldBe` [HiAlfred]
        it "[Aaa] HiAlfred" $ do
            process "Alfred" `shouldBe` [HiAlfred]
        it "[AAA] HiAlfred" $ do
            process "ALFRED" `shouldBe` [HiAlfred]

        it "[aaa] ByeAlfred" $ do
            process "adios alfred" `shouldBe` [ByeAlfred]
        it "[aáa] ByeAlfred" $ do
            process "adiós alfred" `shouldBe` [ByeAlfred]
        it "[Aaa] ByeAlfred" $ do
            process "Adios Alfred" `shouldBe` [ByeAlfred]
        it "[AAA] ByeAlfred" $ do
            process "ADIOS ALFRED" `shouldBe` [ByeAlfred]
        it "[AÁA] ByeAlfred" $ do
            process "ADIÓS ALFRED" `shouldBe` [ByeAlfred]

        {- IO -}
        
        it "[aaa] Write" $ do
            process "escribe hola alfred" `shouldBe` [Write "hola alfred"]
        it "[Aaa] Write" $ do
            process "Escribe Hola Alfred" `shouldBe` [Write "Hola Alfred"]
        it "[AAA] Write" $ do
            process "ESCRIBE HOLA ALFRED" `shouldBe` [Write "HOLA ALFRED"]

        it "[aaa] ShowType" $ do
            process "muestra el tipo de alfred" `shouldBe` [ShowType "alfred"]
        it "[Aaa] ShowType" $ do
            process "Muestra el tipo de Alfred" `shouldBe` [ShowType "alfred"]
        it "[AAA] ShowType" $ do
            process "MUESTRA EL TIPO DE ALFRED" `shouldBe` [ShowType "alfred"]

        it "[aaa] ShowValue" $ do
            process "muestra el valor de alfred" `shouldBe` [ShowValue "alfred"]
        it "[Aaa] ShowValue" $ do
            process "Muestra el valor de Alfred" `shouldBe` [ShowValue "alfred"]
        it "[AAA] ShowValue" $ do
            process "MUESTRA EL VALOR DE ALFRED" `shouldBe` [ShowValue "alfred"]

        it "[aaa] ShowVariable" $ do
            process "muestra la variable alfred" `shouldBe` [ShowVariable "alfred"]
        it "[Aaa] ShowVariable" $ do
            process "Muestra la variable Alfred" `shouldBe` [ShowVariable "alfred"]
        it "[AAA] ShowVariable" $ do
            process "MUESTRA LA VARIABLE ALFRED" `shouldBe` [ShowVariable "alfred"]
    
        {- MEMORIES -}
        
        it "[aaa] DefineMoment" $ do
            process "define este momento como alfred" `shouldBe` [DefineMoment "alfred"]
        it "[Aaa] DefineMoment" $ do
            process "Define este momento como Alfred" `shouldBe` [DefineMoment "alfred"]
        it "[AAA] DefineMoment" $ do
            process "DEFINE ESTE MOMENTO COMO ALFRED" `shouldBe` [DefineMoment "alfred"]

        it "[aaa] GotoMoment" $ do
            process "vete a alfred" `shouldBe` [GotoMoment "alfred"]
        it "[Aaa] GotoMoment" $ do
            process "Vete a Alfred" `shouldBe` [GotoMoment "alfred"]
        it "[AAA] GotoMoment" $ do
            process "VETE A ALFRED" `shouldBe` [GotoMoment "alfred"]

        {- STANDARD -}
                
        it "[aaa] DefineVariable: como Texto" $ do
            process "define la variable alfred como alfred" `shouldBe` [DefineVariable "alfred" (Texto "alfred")]
        it "[Aaa] DefineVariable: como Texto" $ do
            process "Define la variable Alfred como Alfred" `shouldBe` [DefineVariable "alfred" (Texto "Alfred")]
        it "[AAA] DefineVariable: como Texto" $ do
            process "DEFINE LA VARIABLE ALFRED COMO ALFRED" `shouldBe` [DefineVariable "alfred" (Texto "ALFRED")]
        
        it "[aaa] DefineVariable: igual a Texto" $ do
            process "define la variable alfred igual a alfred" `shouldBe` [DefineVariable "alfred" (Texto "alfred")]
        it "[Aaa] DefineVariable: igual a Texto" $ do
            process "Define la variable Alfred igual a Alfred" `shouldBe` [DefineVariable "alfred" (Texto "Alfred")]
        it "[AAA] DefineVariable: igual a Texto" $ do
            process "DEFINE LA VARIABLE ALFRED igual a ALFRED" `shouldBe` [DefineVariable "alfred" (Texto "ALFRED")]
                            
        it "[aaa] DefineVariable: como Entero" $ do
            process "define la variable alfred como 10" `shouldBe` [DefineVariable "alfred" (Entero 10)]
        it "[Aaa] DefineVariable: como Entero" $ do
            process "Define la variable Alfred como 10" `shouldBe` [DefineVariable "alfred" (Entero 10)]
        it "[AAA] DefineVariable: como Entero" $ do
            process "DEFINE LA VARIABLE ALFRED COMO 10" `shouldBe` [DefineVariable "alfred" (Entero 10)]
        it "[Aa-] DefineVariable: como Entero" $ do
            process "Define la variable Alfred como -10" `shouldBe` [DefineVariable "alfred" (Entero (-10))]

        it "[aaa] DefineVariable: igual a Entero" $ do
            process "define la variable alfred igual a 10" `shouldBe` [DefineVariable "alfred" (Entero 10)]
        it "[Aaa] DefineVariable: igual a Entero" $ do
            process "Define la variable Alfred igual a 10" `shouldBe` [DefineVariable "alfred" (Entero 10)]
        it "[AAA] DefineVariable: igual a Entero" $ do
            process "DEFINE LA VARIABLE ALFRED igual a 10" `shouldBe` [DefineVariable "alfred" (Entero 10)]
        it "[Aa-] DefineVariable: igual a Entero" $ do
            process "Define la variable Alfred igual a -10" `shouldBe` [DefineVariable "alfred" (Entero (-10))]
