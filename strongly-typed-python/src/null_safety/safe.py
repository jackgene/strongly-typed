from typing import Optional


text: str = "Lorem Ipsum"
optional_text: Optional[str] = None

print(text.upper())
if optional_text:
    print(optional_text.upper())
