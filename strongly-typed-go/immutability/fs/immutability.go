package main

import (
	"embed"
	"io/fs"
	"io/ioutil"
	"log"
	"os"
)

//go:embed embedded/*
var fileSys embed.FS

func main() {
	fs.ErrNotExist = nil                            // <-- Go lets you do this
	file, err := fileSys.Open("embedded/xyz") // <-- This file does not exist
	if os.IsNotExist(err) {                         // <-- fs.ErrNotExist has changed, condition is false
		log.Printf("Can't open file: %v\n", err)
		return
	}

	bytes, err := ioutil.ReadAll(file) // <-- Panics trying to read invalid file
	if err != nil {
		log.Printf("Can't read file: %v\n", err)
		return
	}

	println(string(bytes))
}
