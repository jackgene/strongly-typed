package unreachable

fun leftOrRight(left: Boolean): String {
    return if (left) {
        "Left"
    } else {
        "Right"
    }
}

fun main() {
    print(leftOrRight(true))
}
