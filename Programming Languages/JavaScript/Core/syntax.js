
// ==============================
// ========== COMMENTS ==========
// ==============================

// single line comment starting with //

/* multi-line comment
can span multiple lines
*/



// ===============================
// ========== VARIABLES ==========
// ===============================

// Delacaration
let block_variable; // block-scoped variable, only accessible within the block they are defined in like function, if statement, loop, etc.
var function_variable; // function-scoped variable, accessible within the function it is defined even if defined within a block
const constant_variable = null; // block-scoped constant, must be initialized at declaration and cannot be reassigned
let inline_declaration = 42; // inline declaration and initialization for both let and var
let var1, var2 = 'Hello', var3="key3"; // multiple declarations in a single statement
let [a=0, b, ...rest] = [1, 2, 3]; // array destructuring assignment, assigns every element of the array to corresponding variable, with rest operator collecting remaining unassigned elements into an array which can be empty, additional variables without corresponding elements will be assigned undefined or default values if provided
let {key1=1, key2:b, [var3], ...rest} = {key1: 1, key2: 2, key3: 3}; // object destructuring assignment, assigns values of object properties to corresponding variables (which can be renamed using :) by matching property names (which can be evaluted if not direct value using []), with rest operator collecting remaining unassigned properties into an object which can be empty, additional variables without corresponding properties will be assigned undefined or default values if provided

// Types and Literals
let int = 10_000_00; // integer number, underscores can be used as separators for better readability
let float = 10.5; // floating-point number, underscores can be used like integers
let infinity = Infinity; // special numeric value representing infinity
let nan = NaN; // special numeric value representing "Not-a-Number"
let bigint = 9007199254740991n; // BigInt for representing integers larger than 2^53 - 1 using 'n' suffix or using BigInt() constructor, underscores can be used like integers
let string_double = "Hello, World!"; // string using double quotes
let string_single = 'Hello, World!'; // string using single quotes
let template_string = `Hello, ${string_single}!`; // template string using backticks allows for interpolation of values using ${}
let boolean = true; // boolean value, can be either true or false
let null_value = null; // special value representing "no value"
let undefined_value = undefined; // special value representing "not assigned"
let array = [1, 2, 3]; // array, an ordered collection of values
let object = { key: 'value', "string key": 42 }; // object, a collection of key-value pairs, keys can only be strings or valid identifiers which convert to strings implicitly



// ===============================
// ========== OPERATORS ==========
// ===============================

// Arithmetic Operators
let sum = 5 + 3; // addition
let difference = 5 - 3; // subtraction
let product = 5 * 3; // multiplication
let quotient = 5 / 3; // division
let remainder = 5 % 3; // modulus
let exponentiation = 5 ** 3; // exponentiation
let prefix_increment = ++sum; // prefix increment, increments value before using it
let postfix_increment = sum++; // postfix increment, increments value after using it
let prefix_decrement = --difference; // prefix decrement, decrements value before using it
let postfix_decrement = difference--; // postfix decrement, decrements value after using it
let unary_minus = -product; // unary minus, negates the value
let unary_plus = +quotient; // unary plus, converts the operand to a number
let coalescing = null_value ?? 'default'; // nullish coalescing operator, returns right operand if left is null or undefined
let ternary = (5 > 3) ? 'yes' : 'no'; // ternary operator, returns value after ? if condition is true, otherwise returns value after :

// Comparison Operators
let equal = 5 == '5'; // loose equality, compares values after type coercion
let strict_equal = 5 === 5; // strict equality, compares values and types without type coercion
let not_equal = 5 != '5'; // loose inequality, compares values after type coercion
let strict_not_equal = 5 !== 5; // strict inequality, compares values and types without type coercion
let greater_than = 5 > 3; // greater than
let less_than = 5 < 3; // less than
let greater_than_equal = 5 >= 3; // greater than or equal to
let less_than_equal = 5 <= 3; // less than or equal to

// Logical Operators
let logical_and = true && false; // logical AND, returns false if first operand is false (short-circuit) or both are false, otherwise returns true
let logical_or = true || false; // logical OR, returns true if first operand is true (short-circuit), otherwise returns false if both are false 
let logical_not = !true; // logical NOT, negates the boolean value

// Bitwise Operators
let bitwise_and = 5 & 3; // bitwise AND
let bitwise_or = 5 | 3; // bitwise OR
let bitwise_xor = 5 ^ 3; // bitwise XOR
let bitwise_not = ~5; // bitwise NOT
let left_shift = 5 << 1; // left shift
let right_shift = 5 >> 1; // right shift
let unsigned_right_shift = 5 >>> 1; // unsigned right shift

// Assignment Operators
let assign = 10; // simple assignment
assign += 5; // addition assignment
assign -= 5; // subtraction assignment
assign *= 5; // multiplication assignment
assign /= 5; // division assignment
assign %= 5; // modulus assignment
assign **= 2; // exponentiation assignment
assign <<= 1; // left shift assignment
assign >>= 1; // right shift assignment
assign >>>= 1; // unsigned right shift assignment
assign &&= 'default'; // logical AND assignment, assigns the result of right operand && left operand to left operand
assign ||= 'default'; // logical OR assignment, assigns the result of right operand || left operand to left operand
assign &= 3; // bitwise AND assignment
assign |= 3; // bitwise OR assignment
assign ^= 3; // bitwise XOR assignment
assign ??= 'default'; // nullish coalescing assignment, assigns right operand if left is null or undefined

// Array Spread Operator
let array2 = [0, ...array, 4, 5]; // array spread operator, expands elements of an array into another array
function_with_params(...array); // using spread operator to pass array elements as individual arguments to a function



// ========================================
// ========== CONTROL STATEMENTS ==========
// ========================================

// If-Else Statement
if (var1 == 0) { // if statement, executes block if condition is true, {} are optional for single statement blocks
    console.log('Condition is zero');
} else if (var1 > 0) { // else if statement, just an if statement as a part of else block, will execute block if condition is true and all previous conditions are false, {} are optional for single statement blocks
    console.log('Condition is positive');
} else { // else statement, executes block if all previous conditions are false, {} are optional for single statement blocks
    console.log('Condition is negative');
}

// Switch Statement
switch (var2) { // switch statement, evaluates expression and executes corresponding case block
    case 'Hello': // case clause, compares switch expression to value using strict equality
        console.log('Greeting detected'); // block executed if case matches
        break; // break statement, exits the switch statement
    case 'See you': // case clause with empty block, falls through to next case without a break
    case 'Goodbye':
        console.log('Farewell detected');
        break;
    default: // default clause, executes if no case matches, optional
        console.log('No match found');
}


// Try-Catch-Finally Statement

// Throw Statement



// ===========================
// ========== LOOPS ==========
// ===========================

// For Loop
for (let i = 0; i < 5; i++) { // for loop, executes block n timees equal to (end - start) / step, first part is initialization, second part is condition, third part is increment/decrement, separated by semicolons, all parts are optional and can be empty, {} are optional for single statement blocks   
    console.log(i); // block executed in each iteration
    if (i === 2) 
        break; // break statement, exits the loop
    else if (i === 3)
        continue; // continue statement, skips the rest of the current iteration and moves to the next iteration
}

// Range-based For Loop
for (const element of [1, 2, 3]) { // range-based for loop, iterates over elements of iterable objects like arrays, strings, maps, sets, etc., each element is assigned to the loop variable in each iteration, {} are optional for single statement blocks, break and continue work like regular for loop
    console.log(element); // block executed in each iteration
}

// While Loop
while (true) { // while loop, executes block as long as condition is true, {} are optional for single statement blocks, break and continue work like regular for loop
    console.log('Infinite loop');
}

// Do-While Loop
do { // do-while loop, executes block at least once and then continues to execute as long as condition is true, {} are optional for single statement blocks, break and continue work like regular for loop
    console.log('This will run at least once');
} while (true); // condition is checked after the block is executed 



// ===============================
// ========== FUNCTIONS ==========
// ===============================

function function_declaration() { // function declaration with no parameters
    return 'Hello'; // return statement, returns value from function and exits the function
}
function function_with_params(param1, param2 = 'default', ...restParams) {
    function_with_params(...param1); // forwarding Rest parameters using spread syntax to another function 
} // function declaration with positional parameter, default parameter, and Rest parameters which collects remaining arguments into an array
const function_expression = function(){}; // anonymous function declation
const named_function_expression = function namedFunc() { // named function expression declaration 
    namedFunc(); // recursive call to the named function expression
}; 
const arrow_function = (param1, param2 = 'default', ...restParams) => 'Hello'; // arrow function with all types of parameters (can be by empty) and implicit return when body is an expression
const arrow_function_block = param => { console.log(param); }; // arrow function with a parameter (parentheses are optional if only one parameter) and a block body which can contain multiple statements and optional return



// =============================
// ========== CLASSES ==========
// =============================

// Class Declaration
class BaseClass { // class declaration
    static static_attribute = 'static value'; // static class attribute, shared among all instances and accessed using the class name, initialization is optional
    static #private_static_attribute = 'private static value'; // private static class attribute, only accessible within the class using # syntax, initialization is optional
    static { // static initialization block, executed once when the class is defined, can be used to define static attributes and methods or perform any setup tasks, can access static attributes and methods using class name or this keyword
        console.log('Static block executed'); // code executed when class is defined
        this.static_attribute2 = true; // defining another static attribute using this keyword
    }
    static static_method() { // static class method, shared among all instances and accessed using the class name, cannot access this keyword, parameters optional
        return this.static_attribute2 ? // access static attribute using class name
            BaseClass.static_attribute : null; // access static attribute using this keyword which refers to the class itself in static methods
    }
    static #private_static_method() { // private static class method, only accessible within the class using # syntax, parameters optional
        return this.#private_static_attribute; // access private static attribute using this keyword which refers to the class itself in static methods
    }

    #private_attribute = 4; // private instance attribute, only accessible within the class using # syntax, each instance has its own copy, initialization is optional
    _attribute = 3; // public instance attribute, accessible from outside the class, each instance has its own copy, initialization is optional
    constructor(param) { // constructor method, called when creating an instance with new keyword, parameters optional
        this.attribute2 = this._attribute; // creating instance attribute directly inside the constructor using this keyword which refers to the instance, initialization is mandatory
        this.attribute2 += this.#private_attribute; // access private instance attribute using this keyword which refers to the instance
    }
    get attribute() { // getter method for attribute, allows accessing attribute like a property while executing code, no parameters allowed, can be static for static attributes
        return this._attribute + 1; 
    }
    set attribute(value) { // setter method for attribute, allows assigning value to attribute like a property while executing code, must have exactly one parameter, can be static for static attributes
        this._attribute = value - 1;
    }
    #private_method() { // private instance method, only accessible within the class using # syntax, parameters optional
        return this.#private_attribute; // access private instance attribute using this keyword which refers to the instance
    }
    method(param) { // method declaration, can be called on instances of the class, parameters optional
        this.attribute = param; // assign to instance attribute to modify it using this keyword
        return this.attribute; // return statement optional, access instance attribute using this keyword
    }
    method2() { 
        this.method(this.attribute + 1); // calling another method of the same class using this keyword 
    }
}
let instance = new BaseClass(10); // creating an instance of the class using new keyword and passing parameters to constructor
instance?. // optional chaining, ?. checks if instance is not null or undefined before accessing method or attribute, otherwise returns undefined
method?.(20);  // optional chaining, ?. checks if method exists before calling it with parameters, otherwise returns undefined

// Inheritance
class DerivedClass extends BaseClass { // class declaration with inheritance using extends keyword
    constructor(param) { // constructor method in derived class, must call super() before using this keyword
        super(param); // call to parent class constructor using super() with all necessary parameters
        this.attribute2 = this.attribute + 1; // create new derived class access and assigne parent class attribute using this to it
    } 
    method(param) { // method overriding, replace parent class method with same name
        this.method2(); // call parent class method using this keyword (when not overridden)
        super.method(param); // call parent class method using super keyword 
    }
}



// =============================
// ========== MODULES ==========
// =============================

// Exporting

// Importing