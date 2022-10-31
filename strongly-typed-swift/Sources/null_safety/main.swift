let text: String? = "..."
if let text = text {
    print(text.uppercased())
}

print(text?.uppercased() ?? "(text was nil)")

//print(text!.uppercased())

//let unsafeText: String! = nil
//print(unsafeText.uppercased())

// Monadic way
let numsByText: [String: Int] = [ "...": -1 ]
let num: Int? = text
    .flatMap { numsByText[$0] }
    .map { $0 * 2 }
print(num ?? 321)
