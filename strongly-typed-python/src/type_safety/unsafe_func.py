from typing import Callable


def run(block: Callable[[int], str]) -> str:
    return block(42)


def valid(num: int) -> str:
    return " " * num


def invalid() -> str:
    return "whatever"


run(invalid)
