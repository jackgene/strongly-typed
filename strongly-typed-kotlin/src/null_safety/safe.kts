val text: String? = "hello"

if (text != null) println(text.uppercase())
val nonNull: String = when(text) {
    null -> "(n/a)"
    else -> text
}