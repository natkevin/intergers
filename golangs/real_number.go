package main

import "fmt"

func check_real_number_01(number int) string {
	/*
	The method for checking the real number is POSITVE/NEGATIVE
	INPUT:
		- number : numeric
	OUPUT:
		- information : string
	*/

	var msg = "The Positive Number"
	if number < 0 {
		msg = "The Negative Number"
	}
	return msg
}

func main() {
	fmt.Println(check_real_number_01(1))
}
