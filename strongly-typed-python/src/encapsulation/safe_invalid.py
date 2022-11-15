class Counter:
    def __init__(self) -> None:
        self._count = 0
    def count(self) -> int:
        return self._count
    def increment(self) -> None:
        self._count += 1

c = Counter()
c._count = -1  # Accessing "private" member
print("Count", c.count())
