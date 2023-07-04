module ExceptionSafety exposing (..)
import Json.Decode

decodedInt : Result Json.Decode.Error Int
decodedInt = Json.Decode.decodeString Json.Decode.int "42"

squared : Int
squared = case decodedInt of
  Ok num -> num * num
  Err _ -> -1
