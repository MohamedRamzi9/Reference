

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

// Declaration 
let block_variable; // block-scoped variable, only accessible within the block they are defined in like function, if statement, loop, etc.
var function_variable; // function-scoped variable, accessible within the function it is defined even if defined within a block
const constant_variable = null; // block-scoped constant, must be initialized at declaration and cannot be reassigned
let inline_declaration = 42; // inline declaration and initialization for both let and var
let var1, var2 = 'Hello', var3; // multiple declarations in a single statement