module Parser.FunctionsSpec where

--------

-- Haskell Libraries
import Test.Hspec                       (describe, it, shouldBe, SpecWith)

--------

-- Alfred Modules
import Core.Parser.Functions (trim)

--------

-- Entrypoint
spec :: SpecWith ()
spec = do
  ----
  describe "Trim :: Remove initial and final blank spaces" $ do
    it "No spaces"                            $ do
      trim "Alfred is cool"           `shouldBe`      "Alfred is cool"
    it "Initial space"                        $ do
      trim " Alfred is cool"          `shouldBe`      "Alfred is cool"
    it "Initial spaces"                       $ do
      trim "   Alfred is cool"        `shouldBe`      "Alfred is cool"
    it "Initial tab"                          $ do
      trim "\tAlfred is cool"         `shouldBe`      "Alfred is cool"
    it "Initial tabs"                         $ do
      trim "\t\tAlfred is cool"       `shouldBe`      "Alfred is cool"
    it "Initial new line"                     $ do
      trim "\nAlfred is cool"         `shouldBe`      "Alfred is cool"
    it "Initial new lines"                    $ do
      trim "\n\nAlfred is cool"       `shouldBe`      "Alfred is cool"
    it "Final space"                          $ do
      trim "Alfred is cool "          `shouldBe`      "Alfred is cool"
    it "Final spaces"                         $ do
      trim "Alfred is cool   "        `shouldBe`      "Alfred is cool"
    it "Final tab"                            $ do
      trim "Alfred is cool\t"         `shouldBe`      "Alfred is cool"
    it "Final tabs"                           $ do
      trim "Alfred is cool\t\t"       `shouldBe`      "Alfred is cool"
    it "Final new line"                       $ do
      trim "Alfred is cool\n"         `shouldBe`      "Alfred is cool"
    it "Final new lines"                      $ do
      trim "Alfred is cool\n\n"       `shouldBe`      "Alfred is cool"
    it "Initial and final single-spaces"      $ do
      trim " Alfred is cool "         `shouldBe`      "Alfred is cool"
    it "Initial and final multi-spaces"       $ do
      trim "  Alfred is cool   "      `shouldBe`      "Alfred is cool"
    it "Initial and final single-tabs"        $ do
      trim "\tAlfred is cool\t"       `shouldBe`      "Alfred is cool"
    it "Initial and final multi-tabs"         $ do
      trim "\t\t\tAlfred is cool\t\t" `shouldBe`      "Alfred is cool"
    it "Initial and final single-new lines"   $ do
      trim "\nAlfred is cool\n"       `shouldBe`      "Alfred is cool"
    it "Initial and final multi-new lines"    $ do
      trim "\n\nAlfred is cool\n\n\n" `shouldBe`      "Alfred is cool"
    it "Inside spaces"                        $ do
      trim "Alfred is  cool"          `shouldBe`      "Alfred is  cool"
    it "Inside tabs"                          $ do
      trim "Alfred\tis\t\tcool"       `shouldBe`      "Alfred\tis\t\tcool"
    it "Inside new lines"                     $ do
      trim "Alfred\nis\n\ncool"       `shouldBe`      "Alfred\nis\n\ncool"
    it "Inside mix of them"                   $ do
      trim "Alfred is\n\tcool"        `shouldBe`      "Alfred is\n\tcool"
    it "External mix of them"                 $ do
      trim " Alfred is cool\n\t"      `shouldBe`      "Alfred is cool"
    it "Final test"                           $ do
      trim "\t Alfred is \n\tcool\n"  `shouldBe`      "Alfred is \n\tcool"
