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



def defun(*args):
    args_list = list(args)
    parameters = args_list[1]
    user_def_funcs[args_list[0]] = lambda *parameters: args_list[2]


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
            # return user_def_funcs[operator](operands)
            # print(user_def_funcs[operator])
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
            defun(*operands)
            return None
        else:
            return [execute_list(item) for item in lst]
    else:
        return lst


def evaluate(instructions):
    if (type(instructions) is str): # an error occurred
        return instructions
    else:
        # func = valid_tokens[instructions[0][0]]
        # print(func)
        result = execute_list(instructions)
        # result = func(*instructions[0][1:])
        return result[0]
    

def format_output(result):
    output_string = ""
    if (isinstance(result, list)):
        output_string = " ".join([str(item) for item in result]).replace("[", "(").replace("]", ")").replace(",", "")
        return "(" + output_string + ")"
    return result


def repl():
    """A simple repl implementation"""
    user_input = ""
    while True:
        user_input = input("lisp >> ").lower()

        if user_input == "quit":
            break

        tokens = tokenize(user_input)
        # print("tokens ", tokens)
        if parenthesis_correct(tokens):
            instructions = translate(tokens)
            # instructions
            # print("instr ",instructions)
            result = evaluate(instructions)
            output = format_output(result)

            print(f"lisp >> {output}")
        else:
            print(f"lisp >> Parenthesis Error")



if __name__ == '__main__':
    repl()