package circle
import "math"

type Circle struct {
	r float64
}
func (c *Circle) Radius() float64 { return c.r }
func (c *Circle) Area() float64 { return math.Pi * c.r * c.r }
func NewCircle(radius float64) *Circle {
	return &Circle{r: radius}
}