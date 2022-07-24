package main

import (
	"fmt"
)

/* Function Sum */
func sum(a, b int) int {
	return (a + b)
}

func main() {
	// Set a and b
	a := 10
	b := 15

	// Display result
	fmt.Print("The Sum of a and num2  = ", sum(a, b))
}
