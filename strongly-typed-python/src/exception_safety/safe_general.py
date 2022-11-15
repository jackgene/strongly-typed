from typing import Callable, TypeVar


T = TypeVar('T')

Try = T | Exception


def safe_try(failable: Callable[..., T], *args: ...) -> Try[T]:
    try:
        return failable(*args)
    except Exception as e:
        return e


num_or_exc: Try[int] = safe_try(int, "non-numeric")
# print(num_or_exc * 2)
if isinstance(num_or_exc, int):
    print(num_or_exc * 2)
else:
    print(f"Unable to parse integer: {num_or_exc}")
