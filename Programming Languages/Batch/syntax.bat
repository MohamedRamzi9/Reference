

@REM variable declaration and assignment
set var=This is a string
@REM variable with quotes 
set var2="This is a quoted string"

@REM using the variable in a command
%var% 

@REM Access arguments passed to the batch file based on their position starting from %1 for the first argument, %2 for the second, and so on.
%1
%2

@REM Remove surrounding quotes from the arguments if they exist
%~1

@REM echoing the variable to the console
echo %var%

@REM If statement, checks if condition is true and executes the block of code accordingly
if "%var%"=="This is a string" (
    @REM This block will execute if the condition is true
    echo The variable matches the expected string.
) else (
    @REM This block will execute if the condition is false
    echo The variable does not match the expected string.
)