//func multiply(_ num1: Any, _ num2: Any) -> Double {
//    num1 * num2
//}
func multiply(_ num1: Any, _ num2: Any) -> Double? {
    guard
        let num1 = num1 as? Double, let num2 = num2 as? Double
    else { return nil }
    return num1 * num2
}

let product: Double? = multiply("42", true)
print(product ?? 0)
