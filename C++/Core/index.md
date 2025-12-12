1. comments
	1. single line comments
	1. multi line comments
1. Main function
1. Variables
	1. declaration
		1. Primitive types
			1. integral 
				1. signed
				1. unsigned
			1. floating point 
			1. boolean 
			1. character 
				1. wchar_t 
				1. char16_t
				1. char32_t
			1. void 
			1. pointer 
			1. array 
			1. lvalue reference
			1. rvalue reference
		1. user defined types
	1. const
	1. volatile
	1. extern
      	1. extern "C"
      	2. extern "C++"
      	3. extern block
	1. static
	2. thread_local
	3. constinit
	4. inline
	5. function pointer
	6. function reference
	7. auto
	8. decltype(auto)
	9. structured binding
		1. parameter pack declaration via structured binding ❌❌❌
	10. pointer to member
	11. pointer to member function
	12. alignas
	13. placeholder variable with no name
2. literals
	1. character literals
	2. integer literals
	3. floating point literals
	4. string literals
	5. boolean literals
	6. null pointer literals
3. initialization
	1. default initialization
	2. direct initialization
	3. value initialization
	4. copy initialization
	5. uniform initialization 
	6. uniform copy initialization
	7. aggregate initialization
	8. designated initialization
4. Operators 
	1. arithmetic 
	2. comparison 
		1. three way comparison
	3. logical 
	4. bitwise 
	5. assignment 
	6. member access 
	7. pointer to member access
	8. deference 
	9. address 
	10. ternary 
	11. comma 
	12. sizeof sizeof...
	13. alignof 
	14. typeid
	15. new, new[], placement new,
	16. delete delete[]
	17. noexcept
	18. scope resolution operator
	19. auto() and auto{}
5. Functions
	1. Function declaration
		1. return type
			1. auto return type
			2. trailing return type
		2. parameters
		3. template arguments
			1. auto arguments
			2. parameter pack
				1. pack indexing
		4. default arguments
		5. concept auto
		6. noexcept specifier
			1. noexcept operator
		7. constexpr specifier
		8. consteval specifier
		9. inline specifier
		10. static specifier
		11. extern specifier
			1. extern "C"
		12. function overloading
		13. deleted functions
	2. function definition
		1. static variables
    1. function with try-catch block
	2. function call
      	1. braced initializer list as argument
6. Types
	1. class and struct
		1. class declaration
			1. alignas specifier
			2. final specifier
			3. replaceable_if_eligible specifier ❌❌❌
			4. trivially_relocatable_if_eligible specifier ❌❌❌
		2. class definition
			1. access specifiers
			2. member variables
				1. mutable variables
			3. static variables
				1. static variables defintion
			4. member functions
				1. explicit this argument
				2. external function declaration 
				3. virtual functions
				4. pure virtual functions
				5. const functions
				6. volatile functions
				7. const volatile functions
				8. &, &&, const &, const && functions qualifiers
				9. static functions
			5. special member functions
				1. explicit constructor
				2. default constructor
				3. copy constructor
				4. copy assignment operator
				5. move constructor
				6. move assignment operator
				7. delegating constructor
			6. destructor
			7. operators overloading 
				1. arithmetic operators
				2. comparison operators
				3. logical operators
				4. conversion operators
				5. call operator
				6. subscript operator
				7. dereference operator
				8. pointer to member operator
				9. static call operator
				10. static subscript operator
				11. comma operator ❌❌❌
				12. new, new[], delete, delete[] operators ❌❌❌
				13. co_await operator ❌❌❌                
			8. default special functions
			9. nested class 
			10. inheritance
				1. using declaration
				2. base class access specifiers
				3. function overriding
				4. virtual inheritance
				5. multiple inheritance
				6. base class access from object
			11. friend functions
			12. friend class 
		3. static member access
		4. accessing member variables and functions
	2. anonymous class and struct 
	3. union 		
		1. anonymous union
	4. enum
		1. enum declaraion
		2. enum definition
			1. default value 
			2. explicit value
		3. enum class
			1. using enum
		4. enum base type
    5. bit fields ❌❌❌
        1. bit-field declaration
		2. bit-field assignment 
7. control statements
	1. if else
		1. if init statment
		2. structured binding declaration as condition 
	2. if constexpr else
		1. if constexpr init statement
	3. if consteval else
	4. if !consteval else
	5. switch case default break
	6. label goto
	7. return
	8. return void
8. loop statements
	1. for
	2. range for 
		1. range for with initializer
	3. while
	4. do while
	5. break
	6. continue
9.  lambdas
	1. lambda capture
		1. capture all by value and reference
		2. capture by value and reference
		3. init capture
		4. static mutable noexcept
		5. this capture
		6. parameter pack capture and init capture
	2. parameters
		1. deducing this parameter
	3. trailing return type
	4. constexpr and consteval lambdas
	5. lambda calling 
10. namespaces
	1. namespace definition
		1. nested namespace definition
	2. namespace access
	3. inline namespaces
	4. unnamed namespaces
	5. using namespace
	6. namespace alias
11. using 
	1. typedef declaration
		1. variable declaration in typedef ❌❌❌
		2. unnamed struct typedef
	2. alias declaration
	3. using as statement
12. user defined literals
	1. integer literals
	2. floating point literals
	3. string literals
	4. character template literals
13. attributes
	1. [[deprecated]]
	2. [[nodiscard]]
	3. [[maybe_unused]]
	4. [[no_unique_address]]
	5. [[fallthrough]]
	6. [[likely]]
	7. [[unlikely]]
	8. [[carries_dependency]] ❌❌❌
	9. [[assume]]
	10. [[noreturn]]
	11. [[indeterminate]] ❌❌❌
	12. using namespace attributes ❌❌❌
	13. multiple attributes decalaration
14. type casting
	1. static cast
	2. dynamic cast
	3. const cast
	4. reinterpret cast
	5. c style cast
	6. function style cast
15. coroutines
	1. awaitable
	2. promise
	3. co_await
	4. co_yield
	5. co_return
16. concepts
	1. template concepts
17. requires
	1. requires expression
		1. requires expression without parameters
		2. requires expression with parameters
	2. requires clause
		1. variable requires clause
		2. function requires clause
		3. class requires clause
18. static assert
19. decltype specifier
20. templates
	1. template function 
		1. template declaration
      		1. template redeclaration with no <> ❌❌❌ 
		2. template parameter pack and paramter pack
		3. default template parameters
		4. unnamed template paramters 
		5. default unnamed template parameters
		6. auto function parameters 
		7. auto return type
		8. non type tempalate paramters
		9.  auto template parameters
		10. concept auto paramter and pack
		11. template template parameters
		12. concept in template parameters
		13. template function specialization
	2. template classes 
		1. template specialization 
		2. partial template specialization
	3. template variables
	4. lambda template parameters			
21. deduction guides
22. exceptions
	1. throw
	2. rethrow
	3. catch
	4. catch all
23. fold expressions
	1. unary fold expressions (left and right)
	2. binary fold expressions (left and right)
24. preprocessor directives
	1. #define
		1. empty macro
		2. variable macro
		3. function macro
		4. multiline macro 
		5. variadic macro
		6. predefined macros
		7. # and ## operators
	2. #undef
	3. #ifdef #ifndef #elifdef #elifndef  
	4. #include
	5. #line
	6. #embed ❌❌❌
	7. #if #elif #else #endif defined !defined
	8. #error
	9. #warning
	10. #pragma
		1. once
    11. _Pragma ❌❌❌
25. alternative tokens ❌❌❌
26. modules 
	1. module declaration
		1. module interface unit
		2. module implementation unit
		3. module partition
		4. global module fragment
	2. export declaration
		1. export identifier
		2. export block
	3. module import
		1. import declaration
		2. import export declaration
		3. partition import declaration
		4. partition export import declaration
	4. private module fragment ❌❌❌
27. asm declaration ❌❌❌
28. contracts ❌❌❌
29. expansion statements ❌❌❌
30. reflection ❌❌❌
31. 