module ParserSpec where

--------

-- Haskell Libraries
import Test.Hspec

--------

-- Alfred Modules
import Core.Parser

--------

-- Entrypoint
spec :: SpecWith ()
spec = do
  describe "Trim :: Remove initial and final blank spaces" $ do
    it "No spaces"                $ do
      trim "Alfred is cool"   `shouldBe` "Alfred is cool"
    it "Initial space"            $ do
      trim " Alfred is cool"  `shouldBe` "Alfred is cool"
    it "Initial tab"              $ do
      trim "\tAlfred is cool" `shouldBe` "Alfred is cool"
    it "Initial new line"         $ do
      trim "\nAlfred is cool" `shouldBe` "Alfred is cool"
    it "Final space"              $ do
      trim "Alfred is cool "  `shouldBe` "Alfred is cool"
    it "Final tab"                $ do
      trim "Alfred is cool\t" `shouldBe` "Alfred is cool"
    it "Final new line"           $ do
      trim "Alfred is cool\n" `shouldBe` "Alfred is cool"
    it "Initial and final spaces" $ do
      trim " Alfred is cool " `shouldBe` "Alfred is cool"
