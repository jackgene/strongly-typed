val thing: Any = if (Math.random() < 0.5) 42 else "forty-two"

// null if cast fails
val str: String? = thing as? String

if (str != null) {
    str.uppercase()
}
