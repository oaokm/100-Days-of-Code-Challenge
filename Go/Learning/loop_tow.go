//* https://gobyexample.com/if-else

package main

import "fmt"

var number = 2

func main(){
	
	//* part one
	if (number % 2) == 0 {
		fmt.Println(number,"is even")
	} else{
		fmt.Println(number,"is ood")
	}
	
	//* part two
	fmt.Println("-------------")
	
	if 5 != 5 {
		fmt.Println("OK")
	} else if 5 == 5 {
		fmt.Println("OOOKKK")
	} else {
		fmt.Println("NO")
	}
}
