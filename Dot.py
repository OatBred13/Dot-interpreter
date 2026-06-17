from pathlib import *
import time

variables = {}
empty_lines = []
index = 0

def int_convert(value):
    is_error = "false"
    value = value.strip()
    if '"' in value:
        value = value.strip('"')

    try:
        value = int(value)
        return value
    except Exception as e:
        terminal_write(f"Line: {index + len(empty_lines)}. Dot.Type.Error: Cannot convert '{value}' into an integer. Err_cd: 14")
        is_error = "true"

    return is_error

def create_var(name, value):
    math_operation = False
    is_error = False
    
    if value == "null":
        value = None
        variables[name] = value

    elif value.startswith("int."):
        math_operation = True

        start_ixd = value.find("(") + 1
        end_ixd = value.find(")")
        value_convert = value[start_ixd:end_ixd]
        
        if value_convert in variables:
            value_convert = variables[value_convert]

        value_convert = int_convert(value_convert)

        variables[name] = value_convert
            
    elif value.startswith("str.") and '"' in value and '"' in value:
        is_error = "false"
        math_operation = True
        start_ixd = value.find("(") + 1
        end_ixd = value.find(")")
        value = value[start_ixd:end_ixd]
        
        value = value.strip('"')

        if value in variables:
            value = variables[value]

        value = str(value)
        variables[name] = value

    elif value.startswith("str.") and '+' in value:
        math_operation = True
        start_ixd = value.find("(") + 1
        end_ixd = value.find(")")
        value = value[start_ixd:end_ixd]
        name1, name2 = value.split("+")
        name1 = name1.strip()
        name2 = name2.strip()
        
        value = string_var_operations(name1, name2)
        value = value.strip('"')
        value = str(value)

        variables[name] = value
        
    elif value.startswith("bool."):
        math_operation = True
        start_ixd = value.find("(") + 1
        end_ixd = value.find(")")
        value = value[start_ixd:end_ixd]
        if value == "True":
            variables[name] = "True"
        elif value == "False":
            variables[name] = "False"

    elif value.startswith("float."):
        math_operation = True
        start_ixd = value.find("(") + 1
        end_ixd = value.find(")")
        value = value[start_ixd:end_ixd]

        if value in variables:
            value = variables[value]

        try:
            value = float(value)
        except:
            terminal_write(f"Dot.Convert.Error: Cannot convert '{value}' into a float.")
            is_error = "true"
    
    elif "+" in value or "-" in value or "*" in value or "/" in value:
        math_operation = True
        if "+" in value:
            op = "+"
        elif "-" in value:
            op = "-"
        elif "*" in value:
            op = "*"
        elif "/" in value:
            op = "/"
        elif "**" in value:
            op = "**"
        elif "//" in value:
            op = "//"
        else:
            terminal_write(f"Line: {index + len(empty_lines)}. Dot.Syntax.Error: Wrong operand used. Please ensure the math operation is one of these: +, -, /, *, **, //. Err_cd: 16")
            is_error = "true"
            return is_error

        argument_one, argument_two = value.split(op)
        argument_one = argument_one.strip()
        argument_two = argument_two.strip()

        if argument_one in variables:
            argument_one = variables[argument_one]
        else:
            try:
                argument_one = float(argument_one)
            except:
                if argument_one.startswith('"') and argument_one.endswith('"'):
                    argument_one = argument_one.strip('"')
                else:
                    terminal_write(f"Dot.Type.Error: Wrong type assigned. Please ensure that '{argument_one}' is in quotation marks. Err_cd: 5")
                    is_error = "true"
                    return is_error

        if argument_two in variables:
            argument_two = variables[argument_two]
        else:
            try:
                argument_two = float(argument_two)
            except:
                if argument_two.startswith('"') and argument_two.endswith('"'):
                    argument_two = argument_two.strip('"')
                else:
                    terminal_write(f"Dot.Type.Error: Wrong type assigned. Please ensure that '{argument_two}' is in quotation marks. Err_cd: 5")
                    is_error = "true"
                    return is_error

        try:
            if op == "+":
                result = argument_one + argument_two
            elif op == "-":
                result = argument_one - argument_two
            elif op == "*":
                result = argument_one * argument_two
            elif op == "/":
                result = argument_one / argument_two
            elif op == "**":
                result = argument_one ** argument_two
            elif op == "//":
                result = argument_one // argument_two
        except:
            terminal_write(f"Line: {index + len(empty_lines)}. Dot.Syntax.Error: Wrong variable type used in the operation. Please ensure the type of the argument is either an int or a float. Err_cd: 17.")
            is_error = "true"
            return is_error

        try:
            try:
                variables[name] = int(result)
            except:
                variables[name] = float(result)
        except:
            terminal_write("Dot.Type.Error: Cannot convert the sum of given arguments into a float or an integer. Err_cd: 13")
            is_error = "true"
    
    else:
        terminal_write(f"Dot.Type.Error: No type assigned to a {value}, and it isn't a math operation. Please check the type definition. Err_cd: 12, {e}")
        is_error = "true"

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
    is_error = "false"
    try:
        value = variables[name]
        value = type(value)
    except Exception as e:
        terminal_write(f"Line: {index + len(empty_lines)}. Dot.Syntax.Error: '{name}' variable does not exist. Please ensure that the variable exist. Err_cd: 8.")
        is_error = "true"
        value = None

    return value, is_error

def console_read_line(text, name):
    value = input(text)

    if "int." in name:
        try:
            value = int(value)
            variables[name] = value
        except:
            terminal_write(f"Line: {index + len(empty_lines)}. Dot.Type.Error: Cannot convert '{value}' into an integer. Err_cd: 14")
            is_error = "true"

    elif "float." in name:
        try:
            value = float(value)
            variables[name] = value
        except:
            terminal_write(f"Line: {index + len(empty_lines)}. Dot.Type.Error: Cannot convert '{value}' into a float. Err_cd: 15")
            is_error = "true"
    
    else:
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
    is_error = "false"
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
        is_error = "true"

    return jump, is_error

def normalize(value):
        value = value.strip()
        if '"' in value:
            value = value.strip('"')

        if value in variables:
            value = variables[value]
        try:
            value = int(value)

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
    i = start_index + 1
    loop_block = []

    while i < len(lines) and lines[i] != "}":
        loop_block.append(lines[i])
        i += 1

    jump = i + 1

    while evaluate_condition(condition):
        for line in loop_block:
            if line == "loop.break":
                return jump
            parse_and_execute(line)

    return jump

def parse_and_execute(command):
    jump = None
    is_error = "false"
    if command == "}":
        return
    
    elif command.startswith("terminal.writeln."):
        start_ixd = command.find("(") + 1
        end_ixd = command.find(")")
        argument = command[start_ixd:end_ixd]
        
        if argument.startswith(('"')) and argument.endswith(('"')):
            argument = argument[1:-1]
            terminal_write(argument)
            
        elif argument in variables:
            argument_var = variables.get(argument)
            terminal_write(argument_var)

        else:
            terminal_write(f"Line: {index + len(empty_lines)}. Dot.Value.Error: No proper argument given for the terminal.writeln.() function. Err_cd: 2")
            is_error = "true"
    
    elif command.startswith("if."):
        start_ixd = command.find("(") + 1
        end_ixd = command.find(") {")
        new_condition = command[start_ixd:end_ixd]
        jump = condition(new_condition, index)
        return jump
    
    elif command.startswith("while."):
        start_ixd = command.find("(") + 1
        end_ixd = command.find(") {")
        condition_while = command[start_ixd:end_ixd]
        jump = while_loop(condition_while, index)
        return jump

    elif "=" in command:
        name, value = command.split(" = ", 1)
        name = name.strip()
        is_error = create_var(name, value)
        
    elif command.startswith("type."):
        start_ixd = command.find("(") + 1
        end_ixd = command.find(")")
        name = command[start_ixd:end_ixd]
        value, is_error = var_type_get(name)

        if value is not None:
            terminal_write(value)
        else:
            pass
    
    elif command.startswith("terminal.readln."):
        start_ixd = command.find("(") + 1
        end_ixd = command.find(")")
        text_raw = command[start_ixd:end_ixd]
        name, text = text_raw.split("|")
        
        if text.startswith('"') and text.endswith('"'):
            text = text.strip('"')
            console_read_line(text, name)
        
        else:
            terminal_write(f"Line: {lines + len(empty_lines)}. Dot.Syntax.Error: Cannot execute terminal.readline.() using the given argument. Please ensure that the argument is in quotation marks. Err_cd: 7")
            is_error  = "true"
    
    elif command == "dot.(help)":
        terminal_write("dot.(exit) - terminates Dot")
        terminal_write("dot.(runfile) - opens a menu for firstly selecting a file and then executing it")
        terminal_write("dot.(debug) - opens the debug mode")
        terminal_write("dot.(version) - displays the current version of Dot")
        terminal_write("dot.(info) - displays information about Dot.")
        terminal_write("dot.(help) - displays the help information")
        terminal_write("terminal.write.(argument) - writes the given argument in the terminal")
        terminal_write("terminal.readline.(name|question) - aks the user for a value")
        terminal_write("name = type.(value) - creates a variable with the given name, type and value")
        terminal_write("type.(name) - displays the type of a given variable")
        terminal_write("pass - does nothing. Can be used in loops or conditions when no action is required")
        
    elif command.startswith("loop.") and command.endswith("{"):
        start_ixd = command.find("(") + 1
        end_ixd = command.find(") {")
        repetitions = command[start_ixd:end_ixd]
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
        is_error = "true"
        
    if jump is not None:
        jump = 0

    return jump, is_error
        
terminal_write("Dot v.0.6.0")
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
            
            if is_error == "true":
                break

            if jump is not None:
                index = jump + 1
            else:
                index += 1
        end_time = time.perf_counter()
        print(f"Executed in {end_time - start_time:.6f} seconds.")

    elif command == "dot.(version)":
        terminal_write("Dot v.0.6.0")
        
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
                
                if is_error == "true":
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
        argument = "Dot.Syntax.Error: Cannot enter a blank line. Err_cd: 1"
        terminal_write(argument)
        
    parse_and_execute(command)
