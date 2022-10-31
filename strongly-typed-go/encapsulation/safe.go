package main
import "strongly-typed-go/encapsulation/counter"

func main() {
	c := &counter.Counter{}
	//c.count = -1
	print("Count: ", c.Count())
}