package main

import "fmt"

func sum2(bil1, bil2 int) int {
	return (bil1 + bil2)
}

func main() {
	var b = [5]int{10, 5, 6, -7, -8}
	var r int = 0
	r = sum2(b[0], b[1])
	fmt.Println(r)

	r = sum2(r, b[2])
	fmt.Println(r)

	r = sum2(r, b[3])
	fmt.Println(r)

	r = sum2(r, b[4])
	fmt.Println(r)

}
