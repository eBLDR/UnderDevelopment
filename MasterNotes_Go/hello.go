/* To run a program from terminal, go to folder and command "go run file_name.go". Make sure the Go compiler is in the path. */
/* Package declaration, defines the package name. Main package is the starting point to run the program. */
package main

/* Package importing. fmt is a preprocessor command which tells the compiler to include files lying in the package fmt. */
import "fmt"

/* Functions. main function is where the program execution begins. */
func main() {
	/* Displays output. Names starting with capital letter are exported - accessible to the importer of the respective package. */
	fmt.Println("Hello World, Go! here.")
}
