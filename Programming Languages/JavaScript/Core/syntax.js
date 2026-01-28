

// ==============================
// ========== COMMENTS ==========
// ==============================

// single line comment starting with //

/* multi-line comment
can span multiple lines
and is enclosed within /* and */



// ===============================
// ========== VARIABLES ==========
// ===============================

// Delacaration
let block_variable; // block-scoped variable, only accessible within the block they are defined in like function, if statement, loop, etc.
var function_variable; // function-scoped variable, accessible within the function it is defined even if defined within a block
const constant_variable = null; // block-scoped constant, must be initialized at declaration and cannot be reassigned
let inline_declaration = 42; // inline declaration and initialization for both let and var
let var1, var2 = 'Hello', var3; // multiple declarations in a single statement

// Types
let int = 10; // integer number
let float = 10.5; // floating-point number
let infinity = Infinity; // special numeric value representing infinity
let nan = NaN; // special numeric value representing "Not-a-Number"
let bigint = 9007199254740991n; // BigInt for representing integers larger than 2^53 - 1 using 'n' suffix
let string_double = "Hello, World!"; // string using double quotes
let string_single = 'Hello, World!'; // string using single quotes
let template_string = `Hello, ${string_single}!`; // template string using backticks allows for interpolation of values using ${}
let boolean = true; // boolean value, can be either true or false
let null_value = null; // special value representing "no value"
let undefined_value = undefined; // special value representing "not assigned"
let array = [1, 2, 3]; // array, an ordered collection of values
let object = { key: 'value', "string key": 42 }; // object, a collection of key-value pairs, keys can only be strings or valid identifiers which convert to strings implicitly
