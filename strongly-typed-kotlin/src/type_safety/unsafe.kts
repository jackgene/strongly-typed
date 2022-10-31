fun multiply(num1: Any, num2: Any): Double? =
    if (num1 !is Double || num2 !is Double) null
    else num1 * num2

val product: Double? = multiply("42.0", true)
