public struct Counter {
    private(set) var count: Int = 0

    public mutating func increment() {
        count += 1
    }
}

var c = Counter()
c.count = -1
print("Count:", c.count)
