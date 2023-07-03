module TypeSafety exposing (..)

multiply : Float -> Float -> Float
multiply num1 num2 = num1 * num2

product : Float
product = multiply "42" True
