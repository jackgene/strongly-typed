import math
from dataclasses import dataclass
from functools import cached_property

__all__ = []

@dataclass(frozen=True)
class Circle:
    radius: float

    @cached_property
    def area(self):
        return math.pi * self.radius ** 2
