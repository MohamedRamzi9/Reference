
// ==============================
// ========== PACKAGES ==========
// ==============================

// Main Package
package main // used in the main file to indicate that this is the entry point of the program
package folder // used in every other file which must be the same name as the folder the file is in



// ===================================
// ========== MAIN FUNCTION ==========
// ===================================

func main() { // the main function is the entry point of the program, { must be in the same line as the function declaration

} // } can go anywhere



// ===============================
// ========== VARIABLES ==========
// ===============================

// Declaration
var variable int = 10  // variable declaration with a type and initialization, type is optional and can be infered if the variable is initialized, initialization is optional
const constant int = 10 // constant declaration with a type and initialization, type is optional and can be infered since intialization is mandatory
variable := 10 // short variable declaration, can only be used inside functions, type is inferred
var variable1, variable2 = 10, "Hello" // multiple variable declaration with initialization, types are inferred for each variable
var variable1, variable2 int = 10, 20 // multiple variable declaration with initialization and one type at the end, type is optional if all variables are initialized

// Types
var variable int // signed integer variable, is at least 32 bits in size, depends of the system, default initialized to 0
var variable int8 // 8-bit signed integer variable, range: [-128, 128[, default initialized to 0
var variable int16 // 16-bit signed integer variable, range: [-2^15, 2^15[, default initialized to 0
var variable int32 // 32-bit signed integer variable, range: [-2^31, 2^31[, default initialized to 0
var variable int64 // 64-bit signed integer variable, range: [-2^63, 2^63[, default initialized to 0
var variable uint // unsigned integer variable, is at least 32 bits in size, depends of the system, default initialized to 0
var variable uint8 // 8-bit unsigned integer variable, range: [0, 256[, default initialized to 0
var variable uint16 // 16-bit unsigned integer variable, range: [0, 2^16[, default initialized to 0
var variable uint32 // 32-bit unsigned integer variable, range: [0, 2^32[, default initialized to 0
var variable uint64 // 64-bit unsigned integer variable, range: [0, 2^64[, default initialized to 0
var variable float32 // 32-bit floating-point variable, default initialized to 0
var variable float64 // 64-bit floating-point variable, default initialized to 0
var variable bool // boolean variable, can only be true or false, default initialized to false
var variable string // string variable, default initialized to ""
var variable complex64 // 64-bit complex number variable, default initialized to (0+0i)
var variable complex128 // 128-bit complex number variable, default initialized to (0+0i)
var variabel error // error variable, default initialized to nil, used to represent an error condition



// ===============================
// ========== OPERATORS ==========
// ===============================

// Arithmetic Operators
var addtion = 12 + 5 // addition operator, adds two operands of same numeric type or concatenates two string types
var subtraction = 12 - 5 // subtraction operator, subtracts two operands of same numeric type
var multiplication = 12 * 5 // multiplication operator, multiplies two operands of same numeric type
var division = 12 / 5 // division operator, divides two operands of same numeric type, if both operands are integers the result will be an integer with the decimal part truncated
var modulus = 12 % 5 // modulus operator, returns remainder of division of two operands of same integer type
variable++ // increment operator, increases value of variable by 1

// Comparison Operators
var equal = 2 == 2 // equal operator, returns true if both operands are equal
var not_equal = 2 != 2 // not equal operator, returns true if both operands are not equal
var greater_than = 2 > 2 // greater than operator, returns true if the left operand is greater than the right operand
var less_than = 2 < 2 // less than operator, returns true if the left operand is less than the right operand
var greater_than_or_equal = 2 >= 2 // greater than or equal operator, returns true if the left operand is greater than or equal to the right operand
var less_than_or_equal = 2 <= 2 // less than or equal operator, returns true if the left operand is less than or equal to the right operand

// Logical Operators
var logical_and = true && false // logical AND operator, returns false if first operand is false or both operands are false, otherwise returns true
var logical_or = true || false // logical OR operator, returns true if first operand is true or both operands are true, otherwise returns false
var logical_not = !true // logical NOT operator, returns true if operand is false, otherwise returns false
variable-- // decrement operator, decreases value of variable by 1

// Bitwise Operators
var bitwise_and = 12 & 5 // bitwise AND operator, performs bitwise AND on two operands of same integer type
var bitwise_or = 12 | 5 // bitwise OR operator, performs bitwise OR on two operands of same integer type
var bitwise_xor = 12 ^ 5 // bitwise XOR operator, performs bitwise XOR on two operands of same integer type
var bit_clear = 12 &^ 5 // bit clear operator, performs bit clear on two operands of same integer type, clears the bits of the first operand which are set to 1 in the second operand
var left_shift = 12 << 2 // left shift operator, shifts the bits of the first operand to the left by the number of bits specified by the second operand, fills the vacated bits with 0
var right_shift = 12 >> 2 // right shift operator, shifts the bits of the first operand to the right by the number of bits specified by the second operand, fills the vacated bits with 0 for unsigned integers and with the sign bit for signed integers

// Assignment Operators
variable += 5 // addition assignment operator, adds the right operand to the left operand and assigns the result to the left operand
variable -= 5 // subtraction assignment operator, subtracts the right operand from the left operand and assigns the result to the left operand
variable *= 5 // multiplication assignment operator, multiplies the left operand by the right operand and assigns the result to the left operand
variable /= 5 // division assignment operator, divides the left operand by the right operand and assigns the result to the left operand
variable %= 5 // modulus assignment operator, takes the modulus of the left operand by the right operand and assigns the result to the left operand
variable &= 5 // bitwise AND assignment operator, performs bitwise AND on the left operand with the right operand and assigns the result to the left operand
variable |= 5 // bitwise OR assignment operator, performs bitwise OR on the left operand with the right operand and assigns the result to the left operand
variable ^= 5 // bitwise XOR assignment operator, performs bitwise XOR on the left operand with the right operand and assigns the result to the left operand
variable &^= 5 // bit clear assignment operator, performs bit clear on the left operand with the right operand and assigns the result to the left operand
variable <<= 5 // left shift assignment operator, performs left shift on the left operand by the number of bits specified by the right operand and assigns the result to the left operand
variable >>= 5 // right shift assignment operator, performs right shift on the left operand by the number of bits specified by the right operand and assigns the result to the left operand



// ========================================
// ========== CONTROL STATEMENTS ==========
// ========================================

// If-Else If-Else Statement
if variable > 19 { // if statement, { must be in the same line as the if keyword, will execute its block if the condition is true
	fmt.print("true condition") // code to execute if the condition is true
} else if variable < 10 { // else if statement, else if must be in the same line as the closing } of the previous block and { must be in the same line as the else if keyword, will check the condition if the previous if or else if conditions were false and execute its block if the condition is true
	fmt.print("else if condition") // code to execute if the else if condition is true
} else { // else statement, else must be in the same line as the closing } of the previous block and { must be in the same line as the else keyword, will execute its block if all previous if and else if conditions were false
	fmt.print("else condition") // code to execute if all previous conditions were false
} 

// Switch Statement with Expression
switch variable { // switch statement with an expression, { must be in the same line as the switch keyword, will compare the expression with the cases and execute the block of the first matching case
case 10: // case statement, case must be in the same line as the case keyword, will execute its block if the expression matches the case value
	fmt.print("case 10") // code to execute if the case matches
	fallthrough // fallthrough statement, used to transfer control to the next case, must be the last statement in the case block, will not check the next case condition
case 20, 30: // case statement with multiple values
	fmt.print("case 20 or 30") // code to execute if the case matches any of the values
default: // default case, default must be in the same line as the default keyword, will execute its block if no other case matches
	fmt.print("default case") // code to execute if no other case matches
}

// Switch Statement with Initialization
switch variable2 := 10; variable2 { // switch statement with initialization, same as above with initialization statement that must be in the same line as the switch keyword and separated from the expression by a semicolon
}

// Switch Statement without Expression
switch { // switch statement without an expression, equivalent to switch true, will execute the block of the first case whose condition is true, same as if statement
case variable > 19: // case statement with a condition, will execute its block if the condition is true
	fmt.print("case variable > 19")
	fallthrough // fallthrough statement, same as in switch with expression
case variable < 10: // case statement with another condition
	fmt.print("case variable < 10")
default: // default case, will execute its block if no other case condition is true
	fmt.print("default case")
}



// =====================================
// ========== LOOP STATEMENTS ==========
// =====================================

// Simple For Loop
for i := 0; i < 10; i++ { // for loop with initialization and condition and post statement separated by semicolons, { must be in the same line as the for keyword, will execute its block as long as the condition is true
	fmt.print(i) // code to execute in each iteration of the loop 
	if i == 5 { 
		break // break statement, used to exit from the loop
	} else if i == 3 {
		continue // continue statement, used to skip the current iteration and go to the next one
	}
}

// For Loop with just Condition
for variable < 10 { // for loop with just a condition, equivalent to while loop, will execute its block as long as the condition is true, { must be in the same line as the for keyword, continune and break work the same as in simple for loop
	fmt.print(variable) // code to execute in each iteration of the loop
}

// Forever Loop
for { // for with no condition, will execute its block forever, { must be in the same line as the for keyword, equivalent to for true, continune and break work the same as in simple for loop
	break
}

// For Range Loop

// Labeled For Loop



// ===============================
// ========== FUNCTIONS ==========
// ===============================

func function(param1 int, param2 string) float32 { // function declaration with parameters which can be 0, and a return type which can be omitted the function will return nothing, { must be in the same line as the function declaration
	return 0.0 // return statement, can be used to return a value and exit from the function, value can be omitted in void function to exit directly from it 
}
func function_with_multiple_return() (int, string) { // function declaration with multiple return types separated by a comma and enclosed in parentheses
	return 0, "" // return statement with multiple return values separated by a comma
}
var var1, var2 = function_with_multiple_return() // initialization of multiple variables with the return values of a function