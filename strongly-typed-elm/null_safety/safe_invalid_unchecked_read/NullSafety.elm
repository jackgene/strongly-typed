module NullSafety exposing (..)

text : Maybe String
text = Nothing

upperText : String
upperText = String.toUpper text
