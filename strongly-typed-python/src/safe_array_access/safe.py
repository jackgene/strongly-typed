from typing import Optional, TypeVar
T = TypeVar("T")

def safe_get(xs: list[T], idx: int) -> Optional[T]:
    return xs[idx] if -len(xs) <= idx < len(xs) else None

words: list[str] = ["one", "two", "three"]
word: Optional[str] = safe_get(words, 3)
if word is not None:
    word = word.upper()
