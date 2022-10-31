package main
import "math"
import "strongly-typed-go/immutability/circle"

func main() {
	//unitCircle := circle.Circle{Radius: 1.0}
	//unitCircle.Radius = 2.0
	unitCircle := circle.NewCircle(1.0)
	unitCircle.r = 2.0
	math.Pi = 0.0
}