import random
from enum import Enum


class Transport(Enum):
    Ground = 1
    Sea = 2


class Status(Enum):
    Active = 1
    Inactive = 2


transport: Transport = random.choice(list(Transport))
status: Status = random.choice(list(Status))

message: str
match (transport, status):
    case (Transport.Ground, Status.Active):
        message = "🚙✅"
    case (Transport.Sea, Status.Active):
        message = "🛳✅"
    case (Transport.Ground, Status.Inactive):
        message = "🚙❌"
    case (Transport.Sea, Status.Inactive):
        message = "🛳❌"
    case _:
        message = "🤷"

print(message)
