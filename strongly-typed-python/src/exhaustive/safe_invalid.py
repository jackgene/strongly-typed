import random
from enum import Enum


class Transport(Enum):
    Ground = 1
    Sea = 2
    Air = 3
    Space = 4


transport: Transport = random.choice(list(Transport))

message: str
match transport:
    case Transport.Ground:
        message = "🚙"
    case Transport.Sea:
        message = "🛳"
    case Transport.Air:
        message = "🛫️"

print(message)
