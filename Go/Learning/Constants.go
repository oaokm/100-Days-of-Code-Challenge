//* https://gobyexample.com/constants

package main

import (
	 "fmt"
	"math"
)
 	
const x string = "constant"


func main() {

	fmt.Println(x)

	const pi = 3.14

	fmt.Println("2pi(sin(35))", (2*pi)*math.Sin(35))
}