class Counter {
    var count: Int = 0
        private set
    fun increment() { if (count < Int.MAX_VALUE) count ++ }
}
val c = Counter()
c.count = -1

println("Count: " + c.count)