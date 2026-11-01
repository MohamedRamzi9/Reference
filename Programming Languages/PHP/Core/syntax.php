<?php // all php code must be contained within php tag

// ============================== 
// ========== COMMENTS ========== 
// ==============================

// this is a single line comment

/* this is a multi-lin comment
it can span multiple lines 
*/



// ==========================
// ========== ECHO ==========
// ==========================

echo "html conetent"; // outputs html content in the place where the echo is used, if the content is a string, remove the quotes and output what is inside, if it's an expression, output the result as a sring, if the result is a boolean, output 1 if true else nothing   



// ===============================
// ========== VARIABLES ==========
// ===============================

// variables always start with $ both in declaration and access

// Declaration
$variable = "value"; // variable declaration, variables can be of any type
$hashtable = array("key" => "value", "key2" => 2); // hashtable variable declaration, each key must be unique and must be a string, integer, or boolean, values are ordered by their insertion order
$array = array(1, "string", 3); // hashtable with default integer keys starting from 0

// Literals
$string = "value"; // string literal
$integer = 10; // integer literal
$float = 4.5; // float literal
$bool = true; $bool = false; // boolean literals
$null = null; // null literal

// Checking functions
$isset = isset($variable); // isset function, returns true if (the variable is declared or a hashtable key exists) and its value is not null
$empty = empty($variable); // empty function, returns true if the variable is not declared, or its value is false, null, empty string, empty hashtable, 0


// ===============================
// ========== OPERATORS ==========
// ===============================

// Arithmetic
$addition = 2 + 2; // addition operator
$subtraction = 2 - 2; // subtraction operator
$multiplication = 2 * 2; // multiplication operator
$division = 2 / 2; // division operator, performs decimal division
$exponentiation = 4 ** 3; // exponentiation operator
$modulo = 4 % 5; // modulo operator, returns the remainder of the division

// Assignment
$addition += 2; // assignment addition operator
$subtraction -= 2; // assignment subtraction operator
$multiplication *= 2; // assignment multiplication operator
$division /= 2; // assignment division operator, performs decimal division
$exponentiation **= 3; // assignment exponentiation operator
$increment++; // increment operator, increases the value of the variable by 1
$decrement--; // decrement operator, decreases the value of the variable by 1

// Comparison
$equal = 2 == 2; // equal operator, returns true if the values are equal, false otherwise, doesn't check for type equality
$identical = 2 === 2; // identical operator, returns true if the values and types are equal, false otherwise
$not_equal = 2 != 2; // not equal operator, returns true if the values are not equal, false otherwise, doesn't check for type equality
$not_identical = 2 !== 2; // not identical operator, returns true if the values or types are not equal, false otherwise
$greater_than = 2 > 2; // greater than operator, returns true if the left value is greater than the right value, false otherwise
$less_than = 2 < 2; // less than operator, returns true if the left value is less than the right value, false otherwise
$greater_than_or_equal = 2 >= 2; // greater than or equal operator, returns true if the left value is greater than or equal to the right value, false otherwise
$less_than_or_equal = 2 <= 2; // less than or equal operator, returns true if the left value is less than or equal to the right value, false otherwise

// Logical 
$and = true && false and true; // logical and operator, returns true if both values are true, false otherwise, short-circuits if the left value is false
$or = true || false or false; // logical or operator, returns true if either value is true, false otherwise, short-circuits if the left value is true
$not = !true; // logical not operator, returns true if the value is false, false otherwise

$string_interpolation = "variable value is {$value}"; // string interpolation, evaluates expression inside {} and replace the {} with the result, $ literal must be preceeded with \ to appear in the string
"string" . "concatenation"; // string concatenation operator, concatenates two strings together, if one value is not a string, it will be converted to a string
$subscript = $array[0]; // subscript operator, accesses the value at the specified key in an hashtable
$coallescing = $variable ?? "default"; // coalescing operator, returns the left value if it exists and is not null, otherwise returns the right value



// ========================================
// ========== CONTROL STATEMENTS ==========
// ========================================

// If statement
if (5 > 3) { // if statement, evaluates the expression inside () that must return a boolean, if true, executes the code inside the if block
    echo "this is true"; // if block, executes if the if statement is true
} elseif (4 == 4) { // elseif statement, only executed when if condition is false, evaluates the expression inside () that must return a boolean, if true, executes the code inside the elseif block, can have multiple elseif statements
    echo "this is false"; // elseif block, executes if the elseif statement is true
} else { // else statement, only executed when if and elseif conditions are false, executes the code inside the else block
    echo "this is false"; // else block, executes if the else statement is true
}

// Switch statement
switch (5) { // switch statement, evaluates the expression inside () and compares it to the case values, executes the code inside the matching case block, if no case matches, executes the code inside the default block
    case 1: // case statement, compares the value of the switch expression to the value of the case expression, if they are equal, executes the code inside the case block
        echo "this is 1"; // case block, executes if the case statement is true
        break; // break statement, exits the switch statement, else will continue executing the next case blocks until a break is encountered or the switch statement ends
    default: // default statement, optional executed if no case matches
        echo "this is default"; // default block, executes if no case matches
}



// ========================================
// ========== CONTROL STATEMENTS ==========
// ========================================

// For loop
for ($i = 0; $i < 10; $i++) { // for loop, executes the code inside the for block a specified number of times, the first expression is executed once before the loop starts, the second expression is evaluated before each iteration, if true, executes the code inside the for block, if false, exits the loop, the third expression is executed after each iteration
    echo $i; // for block, executes if the for statement is true
}

// Foreach loop
foreach ($array as $value) { // foreach loop, iterates over each value in the hashtable and assigns it to the foreach variable, and executes the foreach block for each value
    echo $value; // foreach block
}

foreach ($array as $key => $value) { // same as above but assigns both the key and value to the foreach variables
    echo $key . " => " . $value; // foreach block
}


// while loop
while (true) { // while loop, executes the code inside the while block as long as the expression inside () is true
    echo "this is true"; // while block, executes if the while statement is true
}



// ======================================
// ========== GLOBAL VARIABLES ==========
// ======================================

$_GET; // post super global variable, a hashtable that contains get data from a get request, keys are the names of the get parameters
$_POST; // post super global variable, a hashtable that contains post data from a post request, keys are the ones in the json body of the request




?>