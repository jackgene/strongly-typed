import random

optional_text: str | None = random.choice([None, "lorem ipsum"])
match optional_text:
    case None:
        print("There was nothing")
    case text:
        print(text.upper())
