module InterpreterSpec where

--------

-- Haskell Libraries
import Test.Hspec

--------

-- Alfred Modules
import Core.Interpreter

--------

-- Entrypoint
spec = do
  describe "Eval :: Evaluate the AST of the source code" $ do
    it "Empty Program" $ do
      pending
