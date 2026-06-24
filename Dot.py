# Import all the important modules
from pathlib import *
import time
import sys
import random

# Set the max amount of integer digits in a string, using the sys.set_int_max_str_digits function from the sys library
sys.set_int_max_str_digits(1000000000)
# Create the variable dictionary, empty lines list and the index variable
variables = {}
empty_lines = []
index = 0

def int_convert(value):
    # Sets the is_error variable to False. You're going to see it a lot in this code
    is_error = False

    # Tries to convert the value into an integer, if it can't, it writes an error to the terminal and sets the is_error value to "false"
    try:
        value = int(value)
        return value
    except Exception as e:
        terminal_write(f"Line: {index + len(empty_lines)}. Dot.Type.Error: Cannot convert '{value}' into an integer. Err_cd: 14")
        is_error = True

    return is_error

def addition(numbers):
    result = 0
    for i in numbers:
        result += i

    return result

def subtraction(numbers):
    first_number = numbers[0]
    subtraction_n = 0
    numbers.pop(0)
    for i in numbers:
        subtraction_n += i
    
    result = first_number - subtraction_n
    return result

def mltp(numbers):
    result = 1
    for i in numbers:
        result *= i
    return result

def divide(numbers):
    result = numbers[0]
    
    for num in numbers[1:]:
        if num == 0:
            return "Error: Division by zero."
        result /= num

    return result

def string_convert(argument):
    result = str(argument)
    return result

def float_convert(argument):
    result = float(normalize(argument))
    return result

def parse_argument(input_argument):
    start_ixd = input_argument.find("(") + 1
    end_ixd = input_argument.find(")")
    output_argument = input_argument[start_ixd:end_ixd]

    try:
        output_argument = output_argument.strip('"')
    except:
        pass

    return output_argument

def create_var(name, value):
    # Sets all the handle variables in this function to be false
    math_operation = False
    is_error = False
    
    if value == "null":
        value = None
        variables[name] = value

    elif value.startswith("int."):
        math_operation = True

        value_convert = normalize(parse_argument(value))

        value_convert = int_convert(value_convert)

        variables[name] = value_convert
            
    elif value.startswith("str.") and '"' in value and '"' in value:
        is_error = False
        math_operation = True
        value = parse_argument(value)

        value = string_convert(value)

        variables[name] = value

    elif value.startswith("str.") and '+' in value:
        math_operation = True
        value = parse_argument(value)
        name1, name2 = value.split("+")
        name1 = name1.strip()
        name2 = name2.strip()
        
        value = string_var_operations(name1, name2)
        value = value.strip('"')
        value = str(value)

        variables[name] = value
        
    elif value.startswith("bool."):
        math_operation = True
        value = parse_argument(value)
        if value == "True":
            variables[name] = True
        elif value == "False":
            variables[name] = False

    elif value.startswith("float."):
        math_operation = True
        value = parse_argument(value)

        value = normalize(value)

        try:
            value = float(value)
            variables[name] = value
        except:
            terminal_write(f"Dot.Convert.Error: Cannot convert '{value}' into a float.")
            is_error = True
            return is_error
    
    elif "+" in value or "-" in value or "*" in value or "/" in value or "%" in value:
        math_operation = True
        if "+" in value:
            op = "+"
        elif "-" in value:
            op = "-"
        elif "**" in value:
            op = "**"
        elif "*" in value:
            op = "*"
        elif "//" in value:
            op = "//"
        elif "/" in value:
            op = "/"
        elif "%" in value:
            op = "%"
        else:
            terminal_write(f"Line: {index + len(empty_lines)}. Dot.Syntax.Error: Wrong operand used. Please ensure the math operation is one of these: +, -, /, *, **, //. Err_cd: 16")
            is_error = True
            return is_error

        arguments = value.split(op)

        if op != "**" and op != "//" and op != "%":
            index_loop = 0
            for i in arguments:
                i = i.strip()

            for i in arguments:

                if i in variables:
                    i = int(i)
                else:
                    try:
                        i = normalize(i)
                    except:
                        terminal_write(f"Line: {index + len(empty_lines)}. Dot.Type.Error: Wrong type assigned. Please ensure that '{i}' is in quotation marks, is an integer or float, or is a variable. Err_cd: 6")
                        is_error = True
                        return is_error
                        
                arguments[index_loop] = i
                index_loop += 1
        
        elif op == "**" or op == "%" or op == "//":
            argument_one = arguments[0]
            argument_two = arguments[1]

            argument_one = argument_one.strip()
            argument_two = argument_two.strip()
            try:
                argument_one = normalize(argument_one)
                argument_two = normalize(argument_two)
            except:
                try:
                    argument_one = int(argument_one)
                    argument_two = int(argument_two)
                except:
                    terminal_write(f"Line: {index + len(empty_lines)}. Dot.Type.Error: Wrong type assigned. Please ensure that '{i}' is in quotation marks, is an integer or float or is a variable. Err_cd: 6")
                    is_error = True
                    return is_error

        else:
            terminal_write(f"Line: {index + len(empty_lines)}. Dot.Syntax.Error: Too many or not enough arguments for ** and // math operation. Err_cd: 18")
            is_error = True
            return is_error

        try:
            if op == "+":
                result = addition(arguments)
            elif op == "-":
                result = subtraction(arguments)
            elif op == "*":
                result = mltp(arguments)
            elif op == "/":
                result = divide(arguments)
            elif op == "**":
                result = argument_one ** argument_two
            elif op == "//":
                result = argument_one // argument_two
            elif op == "%":
                result = argument_one % argument_two
        except:
            terminal_write(f"Line: {index + len(empty_lines)}. Dot.Syntax.Error: Wrong variable type used in the operation. Please ensure the type of the argument is either an int or a float. Err_cd: 17.")
            is_error = True
            return is_error

        try:
            try:
                variables[name] = int(result)
            except:
                variables[name] = float(result)
        except:
            terminal_write("Dot.Type.Error: Cannot convert the sum of given arguments into a float or an integer. Err_cd: 13")
            is_error = True
    
    else:
        terminal_write(f"Dot.Type.Error: No type assigned to a {value}, and it isn't a math operation. Please check the type definition. Err_cd: 12")
        is_error = True

    return is_error
            
def string_var_operations(name, name2):
    if name in variables:
        variable_1 = str(variables[name])

    if name2 in variables:
        variable_2 = str(variables[name2])

    if '"' in variable_1:
        variable_1 = variable_1.strip('"')
        variable_1 = str(variable_1)

    if '"' in variable_2:
        variable_2 = variable_2.strip('"')
        variable_2 = str(variable_2)
    
    value = variable_1 + variable_2
    value = f'"{value}"'
    return value

def var_type_get(name):
    is_error = False
    try:
        value = variables[name]
        value = type(value)
    except Exception as e:
        terminal_write(f"Line: {index + len(empty_lines)}. Dot.Syntax.Error: '{name}' variable does not exist. Please ensure that the variable exist. Err_cd: 8.")
        is_error = True
        value = None

    return value, is_error

def read_line(text, name):
    value = input(text)
    
    value = f'str.("{value}")'
    create_var(name, value)

def terminal_write(argument):
    print(argument)
     
def loop_start(repetitions, start_index):
    i = start_index + 1
    loop_block = []

    while lines[i] != "}":
        loop_block.append(lines[i])
        i += 1

    if repetitions == "inf":
        while True:
            for i in loop_block:
                parse_and_execute(i)
                if i == "loop.break":
                    break

    for j in range(repetitions):
        for i in loop_block:
            if i == "loop.break":
                break
            parse_and_execute(i)
                
def condition(condition, start_index):
    is_error = False
    blocks_if_true = []
    blocks_if_false = []
    i = start_index + 1

    while i < len(lines) and lines[i] != "} else {":
        blocks_if_true.append(lines[i])
        i += 1

    if i < len(lines) and lines[i] == "} else {":
        i += 1
        while i < len(lines) and lines[i] != "}":
            blocks_if_false.append(lines[i])
            i += 1

    while i < len(lines) and lines[i] != "}":
        i += 1

    jump = i 

    try:
        result = evaluate_condition(condition)
        if result == True:
            for i in blocks_if_true:
                parse_and_execute(i)
        
        else:
            for i in blocks_if_false:
                parse_and_execute(i)

    except Exception as e:
        terminal_write(f"Line: {index + len(empty_lines)} Dot.Syntax.Error: Condition is not properly formatted. Err_cd: 11. {e}")
        is_error = True

    return jump, is_error

def normalize(value):
        value = value.strip()
        if '"' in value:
            value = value.strip('"')

        if "'" in value:
            value = value.strip("'")

        if value in variables:
            value = variables[value]

        try:
            value = int(value)

        except:
            try:
                value = float(value)
            except:
                pass

        return value

def evaluate_condition(condition):
    
    if "==" in condition:
        value1, value2 = condition.split("==")
        value1 = normalize(value1)
        value2 = normalize(value2)
        return value1 == value2

    elif "!=" in condition:
        value1, value2 = condition.split("!=")
        value1 = normalize(value1)
        value2 = normalize(value2)
        return value1 != value2

    elif "<=" in condition:
        value1, value2 = condition.split("<=")
        value1 = normalize(value1)
        value2 = normalize(value2)
        return value1 <= value2

    elif ">=" in condition:
        value1, value2 = condition.split(">=")
        value1 = normalize(value1)
        value2 = normalize(value2)
        return value1 >= value2

    elif "<" in condition:
        value1, value2 = condition.split("<")
        value1 = normalize(value1)
        value2 = normalize(value2)
        return value1 < value2

    elif ">" in condition:
        value1, value2 = condition.split(">")
        value1 = normalize(value1)
        value2 = normalize(value2)
        return value1 > value2

def while_loop(condition, start_index):
    is_error = False
    i = start_index + 1
    loop_block = []

    while i < len(lines) and lines[i] != "}":
        loop_block.append(lines[i])
        i += 1

    jump = i + 1

    try:
        while evaluate_condition(condition):
            for line in loop_block:
                if line == "loop.break":
                    return jump
                parse_and_execute(line)
    except:
        terminal_write(f"Line: {index + empty_lines}. Dot.Syntax.Error: Condition is not properly formatted. Err_cd: 11")

    return jump, is_error

def parse_and_execute(command):
    return_value = None
    jump = 0
    is_error = False
    if command == "}":
        return
    
    elif command.startswith("writeln."):
        value = parse_argument(command)
        try:
            if value not in variables and value.startswith('"') and value.endswith('"'):
                argument = normalize(value)
                terminal_write(argument)

            elif value in variables:
                value = variables[value]
                terminal_write(value)

            else:
                print(f"Line: {index + len(empty_lines)}. Dot.Value.Error: No proper argument given for the writeln.() function. Err_cd: 2")
                is_error = True
                return is_error

        except:
            print(f"Line: {index + len(empty_lines)}. Dot.Value.Error: No proper argument given for the writeln.() function. Err_cd: 2")
            is_error = True
            return is_error

    elif command.startswith("if."):
        new_condition = parse_argument(command)
        jump = condition(new_condition, index)
        return jump
    
    elif command.startswith("while."):
        condition_while = parse_argument(command)
        jump = while_loop(condition_while, index)
        return jump

    elif "=" in command:
        name, value = command.split(" = ", 1)
        name = name.strip()
        is_error = create_var(name, value)
        
    elif command.startswith("type."):
        name = parse_argument(command)
        value, is_error = var_type_get(name)

        if value is not None:
            terminal_write(value)
        else:
            pass
    
    elif command.startswith("readln."):
        text_raw = parse_argument(command)

        if "|" in text_raw:
            try:
                name, text = text_raw.split("|")
            except:
                terminal_write(f"Line: {index + len(empty_lines)}. Dot.Syntax.Error: No '|' present in terminal.readln.() function.")
                is_error = True
                return is_error
        
            try:
                text = text.strip('"')
                read_line(text, name)

            except:
                terminal_write(f"Line: {index + len(empty_lines)}. Dot.Syntax.Error: Cannot execute readline.() using the given argument. Please ensure that the argument is in quotation marks. Err_cd: 7")
                is_error  = True
                return is_error

        else:
            try:
                text = text_raw.strip('"')
                input(text)
            except:
                terminal_write(f"Line: {index + len(empty_lines)}. Dot.Syntax.Error: Cannot execute readline.() using the given argument. Please ensure that the argument is in quotation marks. Err_cd: 7")
                is_error  = True
                return is_error

    elif command == "dot.(help)":
        terminal_write("dot.(exit) - terminates Dot")
        terminal_write("dot.(runfile) - opens a menu for firstly selecting a file and then executing it")
        terminal_write("dot.(debug) - opens the debug mode")
        terminal_write("dot.(version) - displays the current version of Dot")
        terminal_write("dot.(info) - displays information about Dot.")
        terminal_write("dot.(help) - displays the help information")
        terminal_write("writeln.(argument) - writes the given argument in the terminal")
        terminal_write("readln.(name|argument) - aks the user for a value")
        terminal_write("name = type.(value) - creates a variable with the given name, type and value")
        terminal_write("type.(name) - displays the type of a given variable")
        terminal_write("pass - does nothing. Can be used in loops or conditions when no action is required")
        
    elif command.startswith("loop."):
        repetitions = parse_argument(command)
        if repetitions in variables:
            repetitions = int(variables[repetitions])
        
        else:
            try:
                repetitions = int(repetitions)
            except:
                pass

        loop_start(repetitions, index)

    elif command == "":
        empty_lines.append("_")

    elif command == "dot.(runfile)":
        pass

    elif command == "dot.(debug)":
        pass

    elif command == "pass":
        pass

    elif command.startswith("#"):
        pass

    elif command == "loop.break":
        pass

    elif command == "{" or command == "}":
        pass

    elif command == "exit.()":
        pass

    else:
        terminal_write(f"Line {index + len(empty_lines)}. Dot.Syntax.Error: {command} command does not exist. Err_cd: 3")
        is_error = True

    return jump, is_error
        
terminal_write("Dot v.0.6.5")
terminal_write("For more information visit: https://github.com/OatBred13/Dot-interpreter")
terminal_write("Enter dot.(help) for help.")

while True:

    command = input("<.>>> ")
    
    if command == ("dot.(runfile)"):
        index = 0
        lines = []
        file_path = input("Enter the file's path: ")
        file_name = input("Enter the file's name: ")
        if file_path == "cancel" or file_name == "cancel":
            continue

        try:
            file_final = Path(file_path) / file_name
            with open(file_final, "r") as f:
                lines = [line.strip() for line in f]

        except Exception as e:
            terminal_write(f"Dot.File.Error: Cannot open the file. Please ensure that the file path and name are correct. Err_cd: 10, {e}")

        start_time = time.perf_counter()
        index = 0
        while index < len(lines):
            jump = None
            if lines[index] == "exit.()":
                break
            
            jump, is_error = parse_and_execute(lines[index])
            
            if is_error:
                break

            if jump is not None:
                index = jump + 1
            else:
                index += 1
        end_time = time.perf_counter()
        print(f"Executed in {end_time - start_time:.6f} seconds.")

    elif command == "dot.(version)":
        terminal_write("Dot v.0.6.3")
        
    elif command == "dot.(exit)":
        quit()

    elif command == "dot(info)":
        terminal_write("For more information visit: https://github.com/OatBred13/Dot-interpreter")

    elif command == "dot.(debug)":
        index = 0
        lines = []
        file_path = input("Enter the file's path: ")
        file_name = input("Enter the file's name: ")

        if file_path == "cancel" or file_name == "cancel":
            continue
        try:
            jump = None
            file_final = Path(file_path) / file_name
            with open(file_final, "r") as f:
                lines = [line.strip() for line in f]

            start_time = time.perf_counter()
            index = 0
            while index < len(lines):
                if lines[index] == "exit.()":
                    break

                jump, is_error = parse_and_execute(lines[index])
                
                if is_error:
                    break
                
                if jump is not None:
                    index = jump + 1
                else:
                    index += 1
                print(f"Variables: {variables}")
                print(f"Jump: {jump}")
                print(f"Next command: {lines[index + 1]}")
                input("")
            end_time = time.perf_counter()
            print(f"Executed in {end_time - start_time:.6f} seconds.")

        except Exception as e:
            terminal_write(f"Dot.File.Error: Cannot open the file. Please ensure that the file path and name are correct. Err_cd: 10")

    if command.startswith("#*"):
        while index < len(lines) and "*#" not in lines[index]:
            index += 1
        index += 1
        continue
        
    if not command:
        continue
        
    parse_and_execute(command)
