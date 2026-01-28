
-- ============================
-- ========== IGNORE ==========
-- ============================
function multiple_return()
    return 1, 2, 3
end
local x


-- ================================
-- ========== START HERE ==========
-- ================================



-- ==============================
-- ========== COMMENTS ==========
-- ==============================

-- Single-line comment
--[[
   Multi-line comment
   Can span multiple lines
]]



-- ===============================
-- ========== VARIABLES ==========
-- ===============================

-- Declaration
var = 5 -- declare a global variable
local x = 10 -- declare a local variable that can only be accessed in the current and nested scopes
local a, b = 5, 6 -- multiple declaration assignments, variable names come before the = sign, then their corresponding values, if there are fewer values than names, the remaining names are assigned nil 
local c, d = multiple_return() -- multiple assignment from a function returning multiple values, 

-- Types
int_var = 10 -- integer
float_var = 3.14 -- float
str_var = "Hello" -- string
bool_var = true -- boolean
nil_var = nil -- nil

-- Tables (Lua's only complex data structure)
table_var = { key = "value", [42] = {}, ["4"] = 100 } -- tables which are key-value pairs which both can be of any type except nil and nan for keys, if the key is a valid identifier it can be written without brackets and is interpreted as a string
list_var = {1, 2, 3} -- tables with only values, their keys are implicit integers starting from 1



-- ===============================
-- ========== OPERATORS ==========
-- ===============================

-- Arithmetic
add_result = 5 + 3 -- addition
sub_result = 5 - 3 -- subtraction
mul_result = 5 * 3 -- multiplication
dec_div_result = 5 / 3 -- decimal division
int_div_result = 5 // 3 -- integer division
mod_result = 5 % 3 -- modulus 
exp_result = 5 ^ 2 -- exponentiation

-- Comparison
is_eq = (5 == 5)
is_ne = (5 ~= 3)
lt = (5 < 3)
le = (5 <= 3)
gt = (5 > 3)
ge = (5 >= 3)

-- Logical
and_result = true and false -- logical AND
or_result = true or false -- logical OR
not_result = not true -- logical NOT

-- Bitwise (Lua 5.3+)
bit_and = 5 & 3 -- bitwise AND
bit_or = 5 | 3 -- bitwise OR
bit_xor = 5 ~ 3 -- bitwise XOR
bit_not = ~5 -- bitwise NOT
bit_lshift = 5 << 1 -- left shift
bit_rshift = 5 >> 1 -- right shift

-- Concatenation
concat = "Hello" .. " World" -- string concatenation

-- Length operator
len_list = #list_var -- get the length of a table
len_str = #"abc" -- get the length of a string

-- Table indexing
value = list_var[1] -- returns the values for a given key in a table



-- ========================================
-- ========== CONTROL STATMENETS ==========
-- ========================================

-- all new lines are optional here

-- If-elseif-else
if x > 5 then -- if statement with a condition
    x = x + 1 -- if block that executes if the condition is true
elseif x < 5 then -- elseif statement with another condition, optional
    x = x - 1 -- elseif block that executes if the elseif condition is true and the previous conditions were false
else -- else statement, optional
    x = 0 -- else block that executes if all previous conditions were false
end -- end of if statement

if x == 10 then x = 20 else x = 30 end -- single line if-else statement

-- Goto statement
goto label_name -- jumps to the specified label which can be defined before or after the goto statement
print("This will be skipped") -- this line will be skipped
::label_name:: -- label definition



-- ===========================
-- ========== LOOPS ==========
-- ===========================

-- all new lines are optional here

-- Numeric for loop
for i = 1, 5, 1 do  -- numeric for loop which has four parts : loop variable assigned to start value, end value, step (optional, defaults to 1)
    print(i) -- assigns the next value to the loop variable in each iteration
end -- loop end

-- Generic for loop
function iterator(state, init) -- custom iterator function for generic for loop, state and init are optional if not provided in the for loop
    if init < state then
        return init + 1
    else return nil end 
end
for value in iterator, 10, 0 do -- iterates over values in an iterator function, second and third parts are optional state and init values passed to the iterator function, loop ends when the iterator returns nil
    print(value) -- assigns the next value to the loop variable in each iteration
end -- loop end 

-- While loop
while x < 20 do -- while loop, will only exit when the condition becomes false
    x = x + 1
end -- loop end 

-- Repeat-until loop
repeat -- repeat-until loop, will only exit when the condition becomes true
    x = x - 1 -- loop body will always execute at least once
until x == 10 -- loop condition



-- ===============================
-- ========== FUNCTIONS ==========
-- ===============================

-- Regular functions
function add_three(a, b, c) -- function definition with any number of parameters even zero
    local sum = a + b + c -- local variable inside function scope only visible within the function
    global_sum = sum -- global variable declaration inside function scope visible outside the function
    sum += x -- access to global variable inside function scope
    return a + b + c -- return statement with a single value
end
function multireturn() 
    return 1, 2, 3 -- function return multiple values
end
function noreturn() print("No return value") end -- function with no return statement returns nil by default
function varargs(...) -- function with variable number of arguments, accessed via ... syntax
    local args = {...} -- initialize a table with variable argument pack
    return #args
end

-- Anonymous functions
lambda = function(a) -- anonymous function like a regular function but without a name, can be assigned to variables or passed as arguments 
    return x * 2  -- function can capture variables by reference from surrounding scope, value will be accessed when the function is called
end 

lambda(5) -- calling a function with arguments



-- =========================================
-- ========== TABLES & METATABLES ==========
-- =========================================

-- Methods
function table_var:method(a) -- adds a method to the table which will called on the table itself
    return self.value + a -- self refers to the table the method is called on
end
function table_var.static_method(a) -- adds a static method to the table which is called as a regular function, equivilant to creating a normal function and assigning it to the table as key-value pair
    return a * 2 -- cannot access self
end

-- Metatable mehthods
mt = {} -- a normal table that will be used as a metatable for other tables to overload operators on them
function mt.__add(table, value) table.x = table.x + value end -- overload the + operator
-- same for other binary operators - : __sub, * : __mul, / : __div, // : __idiv, % : __mod, ^ : __pow, .. : __concat, == : __eq, < : __lt, <= : __le, > : __gt, >= : __ge, [] : __index
function mt.__unm(table) table.x = -table.x end -- overload the unary - operator
-- same for other unary operators, not : __not, # : __len
function mt.__call(table, ...) print("function args", ...) end -- overloads call operator on the table
function mt.__newindex(table, key, value) -- overloads assignment to new keys in the table
    rawset(table, key, value) -- use rawset to actually set the key-value pair to avoid infinite recursion
end

setmetatable(table_var, mt) -- assign the metatable to a table, which calls the metamethods when the corresponding operators are used on the table



-- ============================
-- ========== MODULES ==========
-- ============================

local M = {} -- create a table to hold module functions and variables
function M.hello() -- define a function in the module
    print("Hello from module")
end
return M -- return the module table from the file

local m = require("module") -- load the module from another file
m.hello() -- access the module functions and variables



-- ============================
-- ========== COROUTINES ==========
-- ============================

co = coroutine.create(function(x) -- create a coroutine with a function, the arguments will have the values passed to the first call to coroutine.resume
    local sum = 0
    for i = x, x+3 do
        sum = sum + coroutine.yield(i) -- yield returns the value passed to it to the caller of coroutine.resume, then the value passed to the next call of coroutine.resume is returned from coroutine.yield 
    end
end)

status, val = coroutine.resume(co, 1) -- calling the coroutine returns status (true if no error) and the yielded value returned from coroutine.yield or return statement, and passes 1 as the argument to the coroutine function
status, val = coroutine.resume(co, 10) -- resumes the coroutine, which continues execution from the last yield point which will receive 10 as the return value of coroutine.yield



-- ====================================
-- ========== ERROR HANDLING ==========
-- ====================================

function risky()
    error("Something went wrong") -- raises an error with the given value and stops execution and unwinds the stack
end

status, msg = pcall(risky) -- protected call to a function, catches any errors raised and returns status (true if no error) and the error value if any or return value of the function if no error


