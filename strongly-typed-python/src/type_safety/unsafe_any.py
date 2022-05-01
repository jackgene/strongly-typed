from typing import Any


def multiply(num1: Any, num2: Any) -> Any:
    return num1 * num2


product: Any = multiply([1, 2, 3], {"key": "value"})
