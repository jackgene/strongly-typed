import random

thing: int | str = random.choice([42, "forty-two"])

thing.upper()

if isinstance(thing, str):
    thing.upper()
