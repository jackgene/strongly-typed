module NullSafety exposing (..)

text : Maybe String
text = Nothing

upperText : String
upperText = case text of
  Just val -> String.toUpper val
  Nothing -> "(text was absent)"
