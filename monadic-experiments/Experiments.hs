data Expr = Constant Int
    | Add Expr Expr
    | Sub Expr Expr
    | Mult Expr Expr
    | Div Expr Expr
    deriving (Show)

eval :: Expr -> Int
eval (Add  expr1 expr2)  = eval expr1 + eval expr2
eval (Sub  expr1 expr2)  = eval expr1 - eval expr2
eval (Mult expr1 expr2)  = eval expr1 * eval expr2
eval (Div  expr1 expr2)  = eval expr1 `div` eval expr2
eval (Constant expr)     = expr

(//**\\) :: Int -> Int
(//**\\) x = x + 1

(•) :: Num a => a -> a -> a
(•) x y = x * y

(√) :: Floating a => a -> a
(√) = sqrt


main :: IO ()
main = do
    let expr = eval $ Sub (Add (Constant 1) (Constant 2)) (Constant 1)
    print expr
    let x = 0
    print $ (//**\\) x
    print $ 1 • 2
    print $ (√) 16
