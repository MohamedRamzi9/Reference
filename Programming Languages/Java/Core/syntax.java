// continue from : https://docs.oracle.com/javase/tutorial/java/nutsandbolts/arrays.html


// ==============================
// ========== COMMENTS ==========
// ==============================

// this is a single line comment

/* this is 
a multi-line
comment */



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
int difference = x - y; // subtraction
int product = x * y; // multiplication
int quotient = x / y; // division
int remainder = x % y; // modulus
int increment = ++x; // pre-increment, returns the value after incrementing
int decrement = --x; // pre-decrement, returns the value after decrementing
int post_increment = x++; // post-increment, returns the value before incrementing
int post_decrement = x--; // post-decrement, returns the value before decrementing
int negation = -x; // unary negation, returns the negative of the value

// Comparison operators
boolean isEqual = (x == y); // equality
