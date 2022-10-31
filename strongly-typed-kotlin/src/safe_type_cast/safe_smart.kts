val thing: Any = if (Math.random() < 0.5) 42 else "forty-two"

thing.uppercase()

if (thing is String) {
    thing.uppercase()
}
