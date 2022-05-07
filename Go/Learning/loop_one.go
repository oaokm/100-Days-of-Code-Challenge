//* https://gobyexample.com/for

package main

import "fmt"

func main(){

	fmt.Println("----[i loop]----")
	i:=1
	for i <=3{
		fmt.Println(i)
		i = i+1
	}
	
	fmt.Println("----[j loop]----")
	for j:=1; j<=10; j++{
		fmt.Println(j)
	}

	fmt.Println("----[for -> while loop]----")
	z:=1
	for{
		fmt.Println("dd")
		z = z + 1
		if z == 10{
			break
		}
	}

	fmt.Println("----[n loop]----")
	for n:=1; n<=7; n++{
		if n%2 == 0{
			continue
		}
		fmt.Println(n)
	}
}