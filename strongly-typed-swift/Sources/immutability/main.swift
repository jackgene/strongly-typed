struct Circle {
    let radius: Double
    private(set) lazy var area: Double = Double.pi * radius * radius
}

var unitCircle = Circle(radius: 1.0)
unitCircle.radius = 2.0
Double.pi = 0.0
