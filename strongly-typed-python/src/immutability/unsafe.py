import math


def area_of_circle(radius: float) -> float:
    return math.pi * radius * radius


math.pi = 0                # Python lets you do this!
print(area_of_circle(42))  # 0
