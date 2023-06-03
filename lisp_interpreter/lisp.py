import re
from helper_functions import *


valid_tokens = {
    'eq': equals,
    '+': add,
    '-': subtract,
    '/': divide,
    '*': multiply,
    'atom': is_atom,
    'quote': quote,
    '(': '',
    ')': '',
    'cons': cons,
    'cond': cond,
    'car': car,
    'cdr': cdr,
    'defun': 'defun'
}

user_def_funcs = {'dummyKey': 'dummyValue'}


def tokenize(user_input):
    """Turns inputed lisp program into tokens"""
    tokens = user_input.replace('(', ' ( ').replace(')', ' )').replace("'", "quote ").split(' ')
    return [token for token in tokens if token]


def parenthesis_correct(tokens):
    """Returns true if parenthesis are in order. False otherwise."""
    return tokens.count("(") != 0 and tokens.count("(") == tokens.count(")")


def tokens_valid(tokens):
    """Returns True if all the tokens are valid. False otherwise."""
    pattern = r'^[a-zA-Z0-9_()+/*-]+$'
    for token in tokens:
        if (not re.match(pattern, token)) and (token not in valid_tokens.keys()
            and (token not in user_def_funcs.keys())
        ):
            return False
    return True



def translate(tokens):
    """Translates tokens to desired intermidate format"""
    if tokens_valid(tokens):
        converted = []
        stack = []
        for token in tokens:
            if token == '(':
                stack.append([])
            elif token == ')':
                inner_list = stack.pop()
                if stack:
                    stack[-1].append(inner_list)
                else:
                    converted.append(inner_list)
            else:
                if token.isdigit():
                    token = int(token)
                stack[-1].append(token)

        return converted
    else:
        return "Syntax Error Occurred"
    

def create_function(params, body):
    return lambda *args: [body[0], *[arg if arg not in params else args[params.index(arg)] for arg in body[1:]]]


def defun(*args):
    args_list = list(args)
    params = args_list[1]
    body = args_list[2]
    user_def_funcs[args_list[0]] = create_function(params, body)
    return "function created"


def execute_list(lst):
    if isinstance(lst, list):

        if len(lst) == 0: return []
        if lst[0] != 'defun':
            operator = lst[0]
            operands = [execute_list(item) for item in lst[1:]]
        else:
            operator = lst[0]
            operands = lst[1:]
        
        if not isinstance(operator, list) and operator in user_def_funcs.keys():
            for i in range(operands.count("quote")):
                operands.remove("quote")
            if isinstance(operands, list): operands = operands[0]
            return execute_list(user_def_funcs[operator](operands))
        
        if operator == '*':
            return multiply(operands)
        elif operator == '+':
            return add(operands)
        elif operator == '-':
            return subtract(operands)
        elif operator == '/':
            return divide(operands)
        elif operator == 'car':
            return car(operands)
        elif operator == 'cdr':
            return cdr(operands)
        elif operator == 'eq':
            return equals(operands)
        elif operator == 'quote':
            return quote(operands)
        elif operator == 'atom':
            return is_atom(operands)
        elif operator == 'cons':
            return cons(operands)
        elif operator == 'cond':
            return cond(operands)
        elif operator == 'defun':
            return defun(*operands)
        else:
            return [execute_list(item) for item in lst]
    else:
        return lst


def evaluate(instructions):
    if (type(instructions) is str): # an error occurred
        return instructions
    else:
        result = execute_list(instructions)
        return result[0]
    

def format_output(result):
    output_string = ""
    
    if (isinstance(result, list)):
        output_string = " ".join([str(item) for item in result]) \
            .replace("[", "(") \
            .replace("]", ")") \
            .replace(",", "") \
            .replace("True", "t") \
            .replace("False", "()")
        
        return "(" + output_string + ")"
    
    return str(result).replace("True", "t").replace("False", "()")


def repl():
    """A simple repl implementation"""

    count = 1
    user_input = ""

    while True:
        user_input = input(f"lisp[{count}]> ").lower()

        if user_input == "quit":
            break
        if user_input == "clear":
            clear()
            continue

        tokens = tokenize(user_input)

        if parenthesis_correct(tokens):
            instructions = translate(tokens)
            result = evaluate(instructions)
            output = format_output(result)
            print(f"lisp[{count}]> {output}")

        else:
            print(f"lisp[{count}]> Parenthesis Error")
        
        count += 1



if __name__ == '__main__':
    repl()