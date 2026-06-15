# Dot Language Interpreter v0.5.0

Dot Language Interpreter is an interpreter for my programming language Dot, written in Python.

# Features
- Variables
- Variable types (integer, float, string, bool)
- Basic math operations (addition, subtraction, multiplication, division)
- Terminal I/O (`terminal.write.(argument)`, `terminal.readline.(variable name|argument)`)
- Loops (`loop.(n)`, `while.(condition)`)
- Conditions (`if.(condition)`)

# REPL mode
<.>>> x = str.("Hello World!")

<.>>> terminal.write.(x)

Hello World!

# Executing scripts
<.>>> dot.(runfile)

Enter the file's path: scripts/

Enter the file's name: script.txt

# Error list
- Empty line error (only in console mode): *Dot.Syntax.Error: Cannot enter a blank line. Err_cd: 1*

- No proper argument given (for `terminal.write.(argument)`): *Dot.Value.Error: No proper argument given. Err_cd: 2*, Fix: Enter text with quotation marks or enter an existing variable name

- Non existing command (both for console and execution mode): *Line (line number). Dot.Syntax.Error: (non_existing_command) command does not exist. Err_cd: 3*, Fix: Check if the command is written properly

- Cannot convert str to int (both for console and execution mode): *Dot.Convert.Error: Cannot convert string to an integer. Err_cd: 4*, Fix: Enter a number as a string

- A string saved into a variable **without** quotation marks (both for console and execution mode): *Dot.Type.Error: Wrong type assigned. Please ensure that the text value is in quotation marks. Err_cd: 5*, Fix: Enter the text in quotation marks

- Argument in `terminal.readline.(variable_name|argument)` not being in quotation marks (both in console and execution mode): *Dot.Syntax.Error: Cannot execute terminal.readline.() using the given argument. Please ensure that the argument is in quotation marks. Err_cd: 7*, Fix: Make sure the argument is in quotation marks

- Variable does not exist (both in console and execution mode): *Dot.Syntax.Error: Given variable does not exist. Please ensure that the variable exist. Err_cd: 8*, Fix: make sure the variable exist

- Wrong file's name or path: *Dot.File.Error: Cannot open the file. Please ensure that the file path and name are correct. Err_cd: 10*, Fix: make sure that the name and path of the file you're trying to execute are correct

- The condition in `if.(condition) {` is not properly formatted: *Dot.Syntax.Error: Condition is not properly formatted. Err_cd: 11*, Fix: make sure that the condition is in `if.(value1 logic_sign value2)` format.

- No type assigned to a variable: *Dot.Type.Error: No type assigned to a variable, and it isn't a math operation. Please check the type definition. Err_cd: 12*, Fix: make sure that a type is assigned while declaring a variable

- Result of a math operation cannot be stored as a float: *Dot.Type.Error: Cannot convert the sum of given arguments into a float. Err_cd: 13*

# Installation of the interpreter
In the terminal enter this command:
`git clone https://github.com/OatBred13/Dot-interpreter.git`

Or go to [this website](https://github.com/OatBred13/Dot-interpreter.git) and download the lastest release.

# Running the interpeter

You can open the interpreter in two ways. One is through any code editor, and the second one is through the Windows Terminal. To open it using the Windows Terminal, the folder in which the Dot interpreter is located must be found. Then these commands are entered to the terminal:

`cd C:\folder_with_the_Dot_interpreter_file`

`python Dot.py` or `py Dot.py`

# Example code and its execution

## C:\users\user_name\documents\scripts\script.txt

`hello = str.("Hello, ")`

`name = str.("")`

`exclamation_mark = str.("!")`

`terminal.readline.(name|"What is your name?: ")`

`hello_and_name = str.(hello + name)`

`result = str.(hello_and_name + exclamation_mark)`

`terminal.write.(result)`

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
- Nesting (loops/conditions inside of eachother) not fully tested and might be broken
- Some edge cases in conditions and while loops may not work as expected
- Some very specific error cases might not be handled and crash the interpreter

# Reporting bugs
To report bugs either contact underscore bred underscore (Markdown formating couldn't let me write the username normally) on Discord, or contact *u7941919962@gmail.com*.

# Contributing

Pull requests or modification of the Dot interpreter is welcome! For major changed though, please open an issue first.

# License

This project is licensed under the MIT license
