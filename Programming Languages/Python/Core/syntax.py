# ============================
# ========== IGNORE ==========
# ============================
class Class:
	var = 5
	def method(self): pass
	def __and__(self, other): pass
	def __or__(self, other): pass
	def __not__(self): pass
	def __getitem__(self, key): pass
	def __enter__(self): return self
	def __exit__(self, exc_type, exc_value, traceback): pass

obj_var1 = Class()
obj_var2 = Class()
list_var = [2, 3, 4]



# ================================
# ========== START HERE ==========
# ================================



# ==============================
# ========== COMMENTS ==========
# ==============================

# This is a comment, will be ignored by the interpreter

""" 
This is a multi-line string
It can span multiple lines
can be used as a comment when not assigned to a variable
"""



# ==============================
# ========== VARIABLE ==========
# ==============================

# Declaration
var = 5 # variable declaration, can be any valid identifier, 
a, b = 5, 6 # variable declaration with tuple unpacking
a = b = 7 # variable declaration with multiple assignments, starts from the rightmost value and assigns the value to all variables on the left
a: int = 5 # variable declaration with type hints, helps the interpreter and IDEs to understand the type of the variable

# Types
int_var = 8 # decimal literal
int_var = 0o353 # octal literal
int_var = 0x1A3F # hexadecimal literal
int_var = 0b101010 # binary literal

str_var = '9' # string literal
str_var = "Hello, World!" # also string literal
str_var = f'Formatted string with value: {int_var}, {int_var=}, {{{int_var}}}' # formatted string, starts with f, and any expression inside curly braces will be evaluated and inserted into the string after calling str() on the result, adding = after the expression will include the expression itself in the output for debugging purposes, use 3 curly braces to include a literal curly brace in the output, 2 to escape the them for nested expressions
str_var = r'Raw string with backslash \n not interpreted' # raw string, starts with r, and any escape sequences will be treated as literal characters
str_var = '''This is a
multi-line string
using triple quotes.
'''
str_var = fr"""Multi line formatted raw string with value: {int_var} 
and escape sequences not interpreted"""
str_var = f"{{value:[fill][align][sign][#][0][width][grouping][.precision][type]}}" # supports the format specification mini-language


float_var = 10.0 # float literal
float_var = 1.34340e5 # float literal with scientific notation
float_var = 1.34340E5 # same as above

bool_var = True # boolean literal true
bool_var = False # boolean literal false

none_var = None # NoneType literal
ellipsis_var = ... # Ellipsis literal

list_var = [1, 2, 3]  # List
tuple_var = (1, 2, 3)  # Tuple
set_var = {1, 2, 3}  # Set
dict_var = {'key': 'value'}  # Dictionary



# ===============================
# ========== OPERATORS ==========
# ===============================

# Arithmetic operators
add_result = 5 + 3 # addition
sub_result = 5 - 3 # subtraction
mul_result = 5 * 3 # multiplication
div_result = 5 / 3 # decimal division
floor_div_result = 5 // 3 # floor division, returns the integer part of the division
exp_result = 5 ** 3 # exponentiation, raises the first number to the power of the second number
mod_result = 5 % 3 # modulus, returns the remainder of the division

# Comparison operators
eq_result = 5 == 3 # equality
ne_result = 5 != 3 # inequality
lt_result = 5 < 3 # less than
gt_result = 5 > 3 # greater than
le_result = 5 <= 3 # less than or equal to
ge_result = 5 >= 3 # greater than or equal to

chaining_result = 1 < a < 3 # comparison chaining, starts from the leftmost 2 operands and compares them, then use the result of that and compare it with the next operand etc...

# Logical operators
and_result = True and False # logical AND, returns True if both operands are True, and false if the first operand is False or it's true and the second operand is False, not overloadable
or_result = True or False # logical OR, returns True if the first operand is True or it's false and the second operand is True, and False if both operands are False, not overloadable
not_result = not True # logical NOT, returns True if the operand is False, or false if the operand is True

# Bitwise operators
bit_and_result = 5 & 3 # bitwise AND
bit_or_result = 5 | 3 # bitwise OR 
bit_xor_result = 5 ^ 3 # bitwise XOR
bit_not_result = ~5 # bitwise Complement
bit_left_shift_result = 5 << 1 # bitwise left shift
bit_right_shift_result = 5 >> 1 # bitwise right shift

# Compound assignment operators
var = 5
var += 3  # equivalent to var = var + 3
# other compound assignment operators: -=, *=, /=, //=, **=, %=, &=, |=, ^=, <<=, >>=

# Membership access operator
obj_var1.var = 10
obj_var1.method()

walrus_result = (x := 5) + 10 # walrus operator, allows assignment and returns that value in a single expression

is_result = obj_var1 is obj_var2 # is operator, checks if both variables point to the same object in memory
is_not_result = obj_var1 is not obj_var2 # is not operator, checks if both variables do not point to the same object in memory

in_result = 5 in [1, 2, 3, 4, 5] # in operator, checks if the value is present in the iterable
not_in_result = 5 not in [1, 2, 3, 4, 5] # not in operator, checks if the value is not present in the iterable

subscript_result = list_var[2] # subscript operator, arguments can be any valid expression
obj_var1[1, 3] # subscript operator with multiple indices separated by commas

# slice operator
slice_result = list_var[1:3] # slice from [1, 3) (inclusive of 1, exclusive of 3)  
slice_result = list_var[1:] # slice from [1, end of object)
slice_result = list_var[:3] # slice from [beginning of object, 3) 
slice_result = list_var[:] # slice from [beginning of object, end of object)
slice_result = list_var[::2] # specify step, works with all previous slices, used to skip elements if step is greater than 1
slice_result = list_var[::-1] # reverse step, will swap the beginning and end indices of the slice, and use the step as the previous version



# =======================================
# ========== CONTROL STATMENTS ==========
# =======================================

if int_var > 5: # if statement, checks the condition if it is True
	int_var += 1 # if block, executed if the condition is True
elif int_var < 5: # elif statement, optional, checks another condition if the previous one is False
	int_var -= 1 # elif block, executed if the condition is True
else: # else statement, executed if all previous conditions are False
	int_var = 5

int_var = 10 if int_var > 5 else 0 # inline if statement, returns the first value before the if keyword if the condition is True, otherwise returns the second value after the else keyword

with obj_var1 as context: # with statement, calls the __enter__ method of the object at the beginning, if the as part is present assign the return value of __enter__ to the variable context, 
	context.method()
	# calls the __exit__ method of the object at the end of the block, passing any exception that occurred in the block as arguments to the method, if no exception occurred, exc_type, exc_value, and traceback will be None

var = (1, [2, 3])
match var: # match statement, matches the type and value of all nested data members in the object with the patterns in the case blocks
	case 4: pass # case block, executed if the pattern matches the value of the variable
	case (1, [2, 3]): pass
	case _: pass # default case block, executed if no other case matches



# =====================================
# ========== LOOP STATEMENTS ==========
# =====================================

for item in list_var: # for loop, iterates over each item in the object that implements the iterable protocol and put the value in the loop variable 
	if item < 3: # use the value as any variable
		continue # continue statement, skips the rest of the loop body and goes to the next iteration
	elif item == -1:
		break # break statement, exits the loop immediately
	print(item)
else: # else block, executed if the loop completes all iterations without break
	print("Loop completed without break")

while int_var < 10: # while loop, continues as long as the condition is True
	if int_var < 8:
		continue # continue statement, same as for loop
	elif int_var == -1:
		break # break statement, same as for loop
	int_var += 1
else: # else block, executed if loop completes without break
	int_var = 20



# ===============================
# ========== EXCEPTION ==========
# ===============================

try: # try block, contains code that may raise an exception, only one catch block will be executed for the first exception that occurs in the try block
	raise ValueError("This is a value error") # raise statement, raises an exception of the specified type
except ZeroDivisionError as e: # catch block, catches the exception raised in the try block, will get the exception object as e of the specified type or its derived types
	int_var = 0
except Exception as e: # catch any exception, cause all exceptions inherit from Exception
	int_var = -1
else: # else block, executed if no exception occurs in the try block
	int_var = 50
finally: # finally block, always executed regardless of whether an exception occurs or not
	int_var = 100



# ================================
# ========== ASSERTIONS ==========
# ================================

assert int_var > 0, "int_var must be greater than 0" # assert statement, raises AssertionError if the condition is False, error message is optional



# ============================
# ========== DELETE ==========
# ============================

del int_var  # deletes keyword, removes the variable 



# ===============================
# ========== FUNCTIONS ==========
# ===============================

def function(): pass # function with no arguments and no return value, will return None if no return statement is used
def function_return(): # function with no arguments and a return value, any code after return statement is unreachable if it is executed
	return 42 # return statement with a single value
	return 1, 3, 4 # return statement with multiple values, returns a tuple containing the values
def function_return_hint() -> int: # function return with type hint, indicates the retrun type
	return 42

def function_args(arg1, arg2, arg3): # function with mandatory arguments
	return arg1 + arg2 + arg3 # can be used in function body
def function_default_args(arg=None): # function with default argument, if no value is passed when calling the function, will use the default value
	return 0 if arg is None else 4 
def function_positional_args(*args): # function with positional arguments, args is a tuple containing all the arguments passed to the function other than the mandatory ones
	return sum(args) # can be used as a tuple in the function body
def function_keyword_args(**kwargs): # function with keyword arguments, kwargs is a dictionary containing all the keyword arguments passed to the function as a key=value pair
	return sum(kwargs.values()) # can be used as a dictionary in the function body
def function_args_order(arg1, arg2=10, *args, **kwargs): # this is the order of arguments in a function definition: mandatory arguments, default arguments, positional arguments (*args), keyword arguments (**kwargs), any of these can be omitted
	return arg1 + arg2 + sum(args) + sum(kwargs.values())

function_args(1, 2, 3) # function call with mandatory arguments
function_default_args() # function call with default argument
function_default_args(2) # function call with default argument but passing a value
function_positional_args(1, 2, 3, 4, 5) # function call with positional arguments, arguments can be any number of value separated by commas
function_keyword_args(arg1=1, arg2=2, arg3=3) # function call with keyword arguments, arguments are passed as key=value pairs separated by commas
function_args_order("arg1", "default", "pos1", "pos2", key1="value1", key2="value2") # function call with all types of arguments, the first argument is mandatory, the second is default, the third and fourth are positional, and the last two are keyword arguments
function_args(*("pos1")) # function call with tuple unpacking, the number of values in the tuple must match the number of arguments that they occupy
function_args(**{"args": "value1"}) # function call with dictionary unpacking, the keys in the dictionary and number of values must match the names of the function arguments that they occupy  

a = 5
def function_global_nonlocal():
	global a  # uses variable a from the global scope
	a += 1  # modifies global variable a
	b = a # declares a local variable b
	def nested_function(): # nested function definition, only accessible within this function
		nonlocal b # uses variable b from the enclosing function scope 
		global a # uses variable a from the global scope
		b += 1 # modifies local variable b of enclosing function scope
		a += 2 # modifies global variable a
	nested_function() # calling the nested function



# =============================
# ========== LAMBDAS ==========
# =============================

lambda_with_args = lambda x, y: x + y # lambda definition with arguments, can be used called like a regular function, the args come before the : and the body must be a single expression with no return statement, the result of the expression is returned automatically
lambda_no_args = lambda: 42 # lambda definition with no arguments



# =============================
# ========== CLASSES ==========
# =============================

class Base: # class definition
	static = 10 # static data member, shared by all instances of the class
	def __init__(self, value): # __init__ method, called when creating an instance of the class to initialize the instance, self is a reference to the instance being created, can be any name
		self.value = value # adding a data member to the instance if that name does not already exist, since objects are similar to dictionaries
	def method(self): # method definition, can be called on the instance
		return self.value
	@staticmethod # static method decorator used to static methods
	def static_method(): # static method, does not take a first argument by default, can be called both on the class and an instance
		return "This method is called on the class"
	@classmethod # class method decorator used to define class methods
	def class_method(cls): # class method, takes the class that this method is called on as the first argument (important when using inheritance)
		return "This method is called on the class and takes the class as the first argument"
	def __str__(self): # called when using str(obj)
		return f"Value: {self.value}"
	def __repr__(self): # called when using repr(obj)
		return str(self)
	def __add__(self, other): # called when using obj1 + obj2, can return anything
		return Base(self.value + other.value)
		# __sub__ -, __mul__ *, __div__ /, __floordiv__ //, __mod__ %, __pow__ **, __lshift__ <<, __rshift__ >>, __and__ &, __or__ |, __xor__ ^
	def __eq__(self, other): # called when using obj1 == obj2, can return anything
		return self.value == other.value
		# __ne__ !=, __lt__ <, __le__ <=, __gt__ >, __ge__ >=
	def __call__(self, arg): # called when using obj()
		self.value += arg
	def __len__(self): # called when using len(obj)
		return 1
	def __bool__(self): # called when using bool(obj)
		return self.value > 0
	def __hash__(self): # called when using hash(obj)
		return hash(self.value)
	def __iter__(self): # called when using iter(obj)
		return self
	def __next__(self): # called when using next(obj)
		self.value += 1
		return self.value
	def __getitem__(self, key): # called when using obj[key]
		return self.value + key
	def __setitem__(self, key, value): # called when using obj[key] = value
		self.value = value + key
	def __delitem__(self, key): # called when using del obj[key]
		self.value -= key
	def __enter__(self): # called when using with statement 
		return self
	def __exit__(self, exc_type, exc_value, traceback): # called when exiting the with statement block
		pass
	def __contains__(self, item): # called when using in operator
		return item == self.value
	
# Class inheritance
class Derived(Base): # class inheritance, base class go in parentheses separated by commas if multiple, the class inherits all methods and data members from the base classes
	def __init__(self, value, extra): # redefining the __init__ method
		super().__init__(value) # call base class methods with super()
		self.extra = extra + self.value # adding accessing base class data members
	def method(self):  # method overriding, use this method instead of the base class method when called on an instance of this class
		return f"{self.value} and {super().method()}"  # call the base class method using super() to access the base class method in the order of inheritance
	def additional_method(self):
		return f"Extra value: {self.extra}"

base_obj = Base(10) # creating an instance of a class by calling the class like a function
derived_obj = Derived(20, 12)



# ================================
# ========== DECORATORS ==========
# ================================

# Function decorator with no arguments
def decorator(func):
	def wrapper(*args, **kwargs):
		print("Before function call")
		result = func(*args, **kwargs)
		print("After function call")
		return result
	return wrapper

# Function decorator with arguments
def decorator_with_args(arg1, arg2):
	def decorator(func):
		def wrapper(*args, **kwargs):
			print(f"Decorator arguments: {arg1}, {arg2}")
			return func(*args, **kwargs)
		return wrapper
	return decorator

# Class decorator with no arguments
class ClassDecorator:
	def __call__(self, func):
		def wrapper(*args, **kwargs):
			print("Before method call")
			result = func(*args, **kwargs)
			print("After method call")
			return result
		return wrapper

# Class decorator with arguments
class ClassDecoratorWithArgs:
	def __init__(self, arg1, arg2):
		self.arg1 = arg1
		self.arg2 = arg2
	def __call__(self, func):
		def wrapper(*args, **kwargs):
			print(f"Decorator arguments: {self.arg1}, {self.arg2}")
			return func(*args, **kwargs)
		return wrapper

# Decorating functions
@decorator
def decorated_function(x, y):
	return x + y

@decorator_with_args("arg1", "arg2")
def decorated_function_with_args(x, y):
	return x + y

@ClassDecorator()
def class_decorated_function(x, y):
	return x + y

@ClassDecoratorWithArgs("arg1", "arg2")
def class_decorated_function_with_args(x, y):
	return x + y

# Decorating methods
class DecoratedClass:
	@decorator
	def method(self, x, y):
		return x + y
	
	@ClassDecorator()
	def class_method(self, x, y):
		return x + y



# ================================
# ========== GENERATORS ==========
# ================================

def generator_function(x):
	for i in range(x):
		yield i * 2  

gen = generator_function(5)
a = next(gen)  # Get the first value from the generator
for value in gen:  # Iterate through the remaining values
	pass
for value in generator_function(3):  # Iterate through the generator directly
	pass



# =============================
# ========== IMPORTS ==========
# =============================
import math # import statement, adds the module to the current namespace, relative to the parent directory where the main script is run
import .syntax # relative import, . refers to the current package, instead of starting from the root directory, every additional . will go one level up in the directory structure up to maximum of the root directory
from math import sqrt, pi as circle_pi # from import statement, imports specific names from the module into the current namespace separated by commas, which can optionally be renamed using as keyword
from math import ( # use parentheses for multiline import statements, useful for readability 
	sqrt,
	pi,
)
from math import * # from import statement with *, imports all names from the module into the current namespace
import math.pi, math.sqrt as sqrt # accessing a specific name from the module using dot notation, can be nested to access submodules or attributes of the module, unless renamed using as keyword, it must be accessed later using the full imported name
