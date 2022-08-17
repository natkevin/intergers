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
//float64

package main

import (
	"fmt"
)

/* Function Sum */
func sum(a, b float64) float64 {
	return (a + b)
}

func main() {
	// Set a and b
	a := 1.9
	b := 1.9

	// Display result
	fmt.Print("The Sum of a and num2  = ", sum(a, b))
}

