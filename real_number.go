// You can edit this code!
// Click here and start typing.
package main

import "fmt"

func check_real_number_01(number int) string {
	var msg = "The Positive Number"
	if number < 0 {
		msg = "The Negative Number"
	}
	return msg
}

func main() {
	fmt.Println(check_real_number_01(1))
}
