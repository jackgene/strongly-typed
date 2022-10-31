import kotlin.math.PI

data class Circle(val radius: Double) {
    val area: Double by lazy { PI * radius * radius }
}

val unitCircle = Circle(radius = 1.0)
unitCircle.radius = 2.0
PI = 0.0
