https://dev.java/learn/
// excpetions
// lambda expressions
// interfaces
// match statement


// ==============================
// ========== COMMENTS ==========
// ==============================

// this is a single line comment

/* this is 
a multi-line
comment */


// ================================
// ========== MAIN CLASS ==========
// ================================

public class Main { // class containing the starting point of the program, behaves like a regular class
    public static void main(String[] args) { // starting point of the program, the argument (can be named anything) contains command line arguments, first element is the name of the program
        System.out.println("Hello, World!"); // print to console
    }
}



// ===============================
// ========== VARIABLES ==========
// ===============================

// Primitive types
boolean boolean_var; // undefined size, can only hold true or false value, default field value is false
byte byte_var; // 8-bit signed integeral type, default field value is 0
short short_var; // 16-bit signed integeral type, default field value is 0
int int_var; // 32-bit signed integeral type, default field value is 0
long long_var; // 64-bit signed integeral type, default field value is 0L
float float_var; // 32-bit floating point type, default field value is 0.0f
double double_var; // 64-bit floating point type, default field value is 0.0d
char char_var; // 16-bit Unicode character type, default field value is '\u0000'
int[] array_var; // array type, can hold multiple values of the same type


// Declaration
int x; // single declaration
int x = 10; // single declaration with initialization
int x, y = 20; // multiple declaration of same type, every variable can be optionally initialized
final int z = 30; // final declaration, must be initialized at the time of declaration and cannot be changed later 

// Literals
int int_literal = 100; // integer literal, used for int, byte, short, long
int separator_literal = 1_000___000; // use any number of consecutive underscores as a separator for better readability, can be used in any numeric literal
long long_literal = 100L; // long literal, can use 'l' suffix
int hex_literal = 0xFF; // hexadecimal literal
int binary_literal = 0b1010; // binary literal
float float_literal = 3.14F; // float literal, can use 'f' suffix
double double_literal = 3.14; // double literal, can also use 'D' or 'd' suffix
double scientific_literal = 1.23e4; // scientific notation literal
char char_literal = 'A'; // character literal
char unicode_literal = '\u0041'; // Unicode character literal, can be used in string literals
String string_literal = "Hello, World!"; // string literal
Object null_literal = null; // null literal, can be assigned to any reference type
String.class // 🔴🔴🔴



// ===============================
// ========== OPERATORS ==========
// ===============================

// Arithmetic operators
int sum = x + y; // addition
sum += 5; // compound addition
int difference = x - y; // subtraction
difference -= 5; // compound subtraction
int product = x * y; // multiplication
product *= 5; // compound multiplication
int quotient = x / y; // division
quotient /= 5; // compound division
int remainder = x % y; // modulus
remainder %= 5; // compound modulus
int increment = ++x; // pre-increment, returns the value after incrementing
int decrement = --x; // pre-decrement, returns the value after decrementing
int post_increment = x++; // post-increment, returns the value before incrementing
int post_decrement = x--; // post-decrement, returns the value before decrementing
int negation = -x; // unary negation, returns the negative of the value

// Comparison operators
boolean equal = x == y; // equality
boolean not_equal = x != y; // inequality
boolean less_than = x < y; // less than
boolean greater_than = x > y; // greater than
boolean less_than_equal = x <= y; // less than or equal
boolean greater_than_equal = x >= y; // greater than or equal

// Logical operators
boolean and = true && false; // logical AND, doesn't evaluate second operand if the first one is false
boolean or = true || false; // logical OR, doesn't evaluate second operand if the first one is true
boolean not = !true; // logical NOT

// Bitwise operators
int bitwise_and = 3 & 5; // bitwise AND
bitwise_and &= 5; // compound bitwise AND
int bitwise_or = 3 | 5; // bitwise OR
bitwise_or |= 5; // compound bitwise OR
int bitwise_xor = 3 ^ 5; // bitwise XOR
bitwise_xor ^= 5; // compound bitwise XOR
int bitwise_not = ~3; // bitwise NOT
int bitwise_left_shift = 3 << 1; // left shift
bitwise_left_shift <<= 1; // compound left shift
int bitwise_right_shift = 3 >> 1; // right shift
bitwise_right_shift >>= 1; // compound right shift
int bitwise_unsigned_right_shift = 3 >>> 1; // unsigned right shift

String concatenation = "Hello" + " " + "World!"; // string concatenation

int ternary = (x > y) ? x : y; // ternary operator, returns value after ? if condition is true, otherwise returns value after :

boolean instance_of = new Object() instanceof Object; // instance of operator, returns true if the object is an instance of a class, a parent of that class, or implements an interface

(int) 3.14; // type casting, can be used to convert between primitive and user defined types if compatible



// ========================================
// ========== CONTROL STATEMENTS ==========
// ========================================

// If statement
if (x > y) { // if statement, will execute the if block if the condition if true, {} are optional for single statement blocks 
    // if block
} else if (x == y) { // else if statement, optional, it's just an else statement with a single if statement 
    // else if block
} else { // else statement, optional, will execute the else block if the if condition is false, {} are optional for single statement blocks
    // else block
}

// Switch-Case
switch (5) { // switch statment, will execute case statements that match the value of the condition which must be of byte, short, char, int, their corresponding wrapper classes, enum types, String
    case 4: // empty case statement, will fall through to the next case statement
    case 3: // case statement, can contain any number and type of statements
		// code will be executed from here to the end of the switch
		break; // break statement, optional, will exit the switch statement

	default: // default case, will be executed if no case matches, can appear anywhere in the switch statement
}



// =====================================
// ========== LOOP STATEMENTS ==========
// =====================================

// For loop
for (int i = 0; i < 10; i++) { // for loop, initializes a variable, continues excuting for block while the condition is true, and increments the variable at the end of each iteration, {} are optional for single statement blocks
    // for loop block
    break; // break statement, will exit the loop
    continue; // continue statement, will skip the rest of the loop body and go to the next iteration
}
for (;true;) {} // first and third statements are optional

// Range For loop
for (int element : array_var) { // range for loop, iterates over the elements of an iterable object and assigns them to a variable, {} are optional for single statement blocks
    // range for loop block
    break; // break statement, will exit the loop
    continue; // continue statement, will skip the rest of the loop body and go to the next iteration
}

// While loop
while (true) { // while loop, continues excuting while block as long as the condition is true, {} are optional for single statement blocks
    // while loop block
    break; // break statement, will exit the loop
    continue; // continue statement, will skip the rest of the loop body and go to the next iteration
    
}

// =============================
// ========== CLASSES ==========
// =============================

public class MyClass { // class declaration, can be declared as public (in which case can only be one and must be in a file with the same name), private, protected, or none (no modifier)
    int x; // field declaration
    public MyClass() { // constructor declaration, has the same name as the class and no return type
        this.x = 0; // this keyword refers to the current instance of the class, can be omitted when accesing fields and methods if there names are not shadowed by local variables
    }
    int myMethod(int a, int b) { // method declaration, can be declared as public, private, protected, or none (no modifier), can have any return type, or void if it doesn't return anything, and any number of parameters including none
        // method body
        return a + b; // return statement, can appear anywhere in the method body, must have at least one unconditional return statement reachable from any point in the body
    }
    short myMethod() { // method overloading, declares another version of the method with the same name with different parameters and or return type, correct method will be called based on the arguments passed to the method
        // method body
        return (short) (a - b);
    }
    final int myFinalMethod() {} // final method, cannot be overridden by any subclass
}
class MySubClass extends MyClass { // class inheritance, can only extend one class, will inherit all fields and methods from the parent class
    @Override // overried annotation, must be used when overriding a method from the parent class
    int myMethod(int a, int b) { // method overriding, must have same name, return type, and parameters, allows modifying the body of the parent method    
        return super.myMethod(a, b) * 2; // super keyword refers to the parent class, can be used to access fields and methods from the parent class
    }
}
final class MyFinalClass {} // final class, cannot be extended by any other class