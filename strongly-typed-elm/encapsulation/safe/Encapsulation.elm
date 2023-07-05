module Encapsulation exposing (..)
import Counter exposing (Counter)

counter : Counter
counter = Counter.zero

negativeCounter : Counter -> Counter
negativeCounter (Counter.PrivateCounter count) =
  Counter.PrivateCounter -1
