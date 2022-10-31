package main

//import (
//	"strconv"
//	"strings"
//)
//
//func main() {
//	var thing interface{} = 42
//
//	text, _ := thing.(string)      // non-panicking type assertion
//	println(strings.ToUpper(text)) // let's hope zero-value is ok!
//
//	text = thing.(string) // unsafe type assertion - panic!
//	println(strings.ToUpper(text))
//
//	switch data := thing.(type) { // type switch, if only default was required!
//	case int:
//		text = strconv.Itoa(data)
//	}
//	println(text) // let's hope zero-value is Ok!
//
//	text = func() string {
//		switch data := thing.(type) { // type switch returning casted value, default required 🎉
//		case string: return data
//		default: return "oops"
//		}
//	}()
//	println(text)
//}
