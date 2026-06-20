# Dot Language Interpreter v0.6.3

Dot Language Interpreter is an interpreter for a programming language called Dot. The interpreter itself is written in Python.

# Dot v0.6.3 changelog:
- The argument parsing of commands was turned into a function
- The error with entering an empty line in REPL mode was removed 
- The is_error variable is now a bool
- Simple math operation (addition, subtraction, multiplication and division) now supports multiple numbers (2 + 5 + 6, 5 * 3 * 2, etc.)
- terminal.writeln.() and terminal.readln.() Functions were shortened into writeln.() and readln.()
- Expanded the error handling
- Upgraded debug mode

# Features
- Variables
- Variable types (integer, float, string, bool)
- Basic operations on strings
- Script execution & debugging
- Basic math operations (addition, subtraction, multiplication, division, raising to the power, division without a remainder)
- Terminal I/O (`writeln.()`, `readln.()`)
- Loops (`loop.(n)`, `while.(condition)`)
- Conditions (`if.(condition)`)
- Commends (#, #* *#)

# REPL mode
<.>>> x = str.("Hello World!")

<.>>> writeln.(x)

Hello World!

# Executing scripts
<.>>> dot.(runfile)

Enter the file's path: scripts/

Enter the file's name: script.txt

# Error list

- No proper argument given (for `writeln.(argument)`): *Dot.Value.Error: No proper argument given. Err_cd: 2*, Fix: Enter text with quotation marks or enter an existing variable name

- Non-existing command (both for console and execution mode): *Line (line number). Dot.Syntax.Error: (non_existing_command) command does not exist. Err_cd: 3*, Fix: Check if the command is written properly

- A string saved into a variable **without** quotation marks (both for console and execution mode): *Dot.Type.Error: Wrong type assigned. Please ensure that the text value is in quotation marks. Err_cd: 5*, Fix: Enter the text in quotation marks

- An argument in a math operation couldn't be prepared correctly: *Dot.Type.Error: Wrong type assigned. Please ensure that 'value' is in quotation marks, is an integer or float or is a variable. Err_cd: 6*

- Argument in `readlineln.(variable_name|argument)` not being in quotation marks (both in console and execution mode): *Dot.Syntax.Error: Cannot execute terminal.readline.() using the given argument. Please ensure that the argument is in quotation marks. Err_cd: 7*, Fix: Make sure the argument is in quotation marks

- Variable does not exist (both in console and execution mode): *Dot.Syntax.Error: Given variable does not exist. Please ensure that the variable exist. Err_cd: 8*, Fix: make sure the variable exist

- Wrong file's name or path: *Dot.File.Error: Cannot open the file. Please ensure that the file path and name are correct. Err_cd: 10*, Fix: make sure that the name and path of the file you're trying to execute are correct

- The condition in if's or while loops is not properly formatted: *Dot.Syntax.Error: Condition is not properly formatted. Err_cd: 11*, Fix: make sure that the condition is in `if./while.(value1 logic_sign value2)` format.

- No type assigned to a variable: *Dot.Type.Error: No type assigned to a variable, and it isn't a math operation. Please check the type definition. Err_cd: 12*, Fix: make sure that a type is assigned while declaring a variable

- Result of a math operation cannot be stored as a float: *Dot.Type.Error: Cannot convert the sum of given arguments into a float. Err_cd: 13*

- Cannot convert a value into an integer: *Dot.Type.Error: Cannot convert 'value' into an integer. Err_cd: 14*, Fix: Ensure that the given value is a number

- Cannot convert a value into a float: *Dot.Type.Error: Cannot convert 'value' into a float. Err_cd: 15*, Fix: Ensure that the given value is a float number

- Wrong math operand used in a math operation: *Dot.Syntax.Error: Wrong operand used. Please ensure the math operation is one of these: +, -, /, *, **, //. Err_cd: 16*, Fix: Enter a math operand from the given list

- Wrong variable type used in a math operation: *Dot.Syntax.Error: Wrong type used in the operation. Please ensure the type of the argument is either an int or a float. Err_cd: 17*, Fix: Check or change the type of the variables used in the math operation

- Too many arguments used for ** and // math operations: *Dot.Syntax.Error: Too many or not enough arguments for ** and // math operation. Err_cd: 18*, Fix: Check if there are only 2 arguments for these math operations

# Installation of the interpreter
In the terminal, enter this command:
`git clone https://github.com/OatBred13/Dot-interpreter.git`

Or go to [this website](https://github.com/OatBred13/Dot-interpreter.git) and download the latest release.

# Running the interpreter

You can open the interpreter in two ways. One is through any code editor, and the second one is through the Windows Terminal. To open it using the Windows Terminal, the folder in which the Dot interpreter is located must be found. Then these commands are entered into the terminal:

`cd C:\folder_with_the_Dot_interpreter_file`

`python Dot.py` or `py Dot.py`

# Example code and its execution

## C:\users\user_name\documents\scripts\script.txt

`hello = str.("Hello, ")`

`name = str.("")`

`exclamation_mark = str.("!")`

`readln.(name|"What is your name?: ")`

`hello_and_name = str.(hello + name)`

`result = str.(hello_and_name + exclamation_mark)`

`writeln.(result)`

## Console
<.>>> dot.(runfile)

Enter the file's path: 

C:\users\user_name\documents\scripts

Enter the file's name: script.txt

## Output
What is your name?: OatBred

Hello, OatBred!

Executed in 0.001092 seconds.

# Known Issues
- Nesting (loops/conditions inside of each other) is not fully tested and might be broken
- Some edge cases in conditions and while loops may not work as expected

# Reporting bugs

To report bugs, either contact underscore bred underscore (Markdown formatting couldn't let me write the username normally) on Discord, or contact *u7941919962@gmail.com*.

# Contributing & Feeback

Pull requests or modifications to the Dot interpreter are welcome! For major changes, though, please open an issue first.

Feedback is very much welcome, too! If you tried to code something in Dot yourself, and something crashed or didn't work as expected, create an issue or contact me.

# License

This project is licensed under the MIT license
