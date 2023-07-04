module SafeArrayAccess exposing (..)
import Array exposing (Array)

words : Array String
words = Array.fromList ["one", "two", "three"]

word : Maybe String
word = words
  |> Array.get -1
  |> Maybe.map String.toUpper