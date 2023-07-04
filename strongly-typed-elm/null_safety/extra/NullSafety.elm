module NullSafety exposing (..)

import Dict exposing (Dict)

text : Maybe String
text = Just "xyz"

numsByText : Dict String Int
numsByText = Dict.fromList [ ("xyz", 42) ]

num : Maybe Int
num = text
  |> Maybe.andThen (\k -> Dict.get k numsByText)
  |> Maybe.map ((*) 2)
