package main
import "net/url"

func main() {
	url, _ := url.QueryUnescape("bad%url") // error ignored!
	println(url) // let’s hope 0-value is OK!
}
//func main() {
//	url1, err := url.QueryUnescape("good%20enough%21")
//	if err != nil { return }
//	url2, err := url.QueryUnescape("bad%url")
//	println(url1, url2)
//}
