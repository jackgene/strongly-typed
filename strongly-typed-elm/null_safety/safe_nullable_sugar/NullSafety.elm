module NullSafety exposing (..)

text : Maybe String
text = Nothing

upperText : String
upperText = text |> Maybe.map String.toUpper
  |> Maybe.withDefault "(text was absent)"
