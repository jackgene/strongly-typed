package main
import "strings"

func main() {
	var thing interface{} = 42

	str, _ := thing.(string)
	println(strings.ToUpper(str))

	str = thing.(string)
}
