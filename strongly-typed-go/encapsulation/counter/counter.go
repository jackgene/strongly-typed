package counter
import "math"

type Counter struct {
	countx int
}

func (c *Counter) Count() int { return c.countx }
func (c *Counter) Increment() {
	if c.countx < math.MaxInt { c.countx ++ }
}