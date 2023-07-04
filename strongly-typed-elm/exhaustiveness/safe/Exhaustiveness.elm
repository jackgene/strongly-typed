module Exhaustiveness exposing (..)

type Status = Active | Inactive
type Membership = Basic | Premium

doWork : Status -> Membership -> String
doWork status membership =
  case (status, membership) of
    (Active, Basic) -> "Perform basic API calls..."
    (Active, Premium) -> "Perform premium API calls..."
    (Inactive, Basic) -> "Skipping..."
    (Inactive, Premium) -> "Skipping..."
