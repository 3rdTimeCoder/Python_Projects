from helper_functions import *


# valid_tokens = ['eq', '+', '-', '/', '*', 'atom', 'quote', '(', ')', 'cons', 'car', 'cdr']
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
    'car': car,
    'cdr': cdr,
    'defun': 'defun'
}



def tokenize(user_input):
    """Turns inputed lisp program into tokens"""
    tokens = user_input.replace('(', ' ( ').replace(')', ' )').replace("'", "quote ").split(' ')
    return [token for token in tokens if token]


def parenthesis_correct(tokens):
    """Returns true if parenthesis are in order. False otherwise."""
    return tokens.count("(") != 0 and tokens.count("(") == tokens.count(")")


def tokens_valid(tokens):
    """Returns true if all the tokens are valid. False otherwise."""
    for token in tokens:
        if (token not in valid_tokens.keys() and not token.isalnum()):
            return False
    return True


# def translate(tokens):
#     """Translates tokens into intermediate form"""
#     if tokens_valid(tokens):
#         instructions = []
#         while tokens:
#             token = tokens[0]

#             if token != '(' and token != ')':
#                 if token in valid_tokens.keys():
#                     instruction = valid_tokens[token]
#                 elif token.isdigit():
#                     instruction = int(token)
#                 else:
#                     instruction = token

#                 instructions.append(instruction)
#                 tokens.pop(0)

#             elif token == '(':
#                 nested_tokens = tokens[1:]
#                 nested_instructions = translate(nested_tokens)
#                 instructions.append(nested_instructions)
#                 tokens = nested_tokens[len(nested_instructions):]

#             elif token == ')':
#                 tokens.pop(0)
#                 break

#         if 'quote' in instructions:
#             quote_index = instructions.index('quote')
#             quoted_expression = instructions[quote_index+1]
#             instructions = ['quote', quoted_expression]

#         return instructions

#     else:
#         return "Syntax Error Occurred"


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


def evaluate(instructions):
    if (type(instructions) is str): # an error occurred
        return instructions
    else:
        func = valid_tokens[instructions[0][0]]
        print(func)
        result = func(*instructions[0][1:])
        return result


def repl():
    """A simple repl implementation"""
    user_input = ""
    while True:
        user_input = input("lisp >> ").lower()

        if user_input == "quit":
            break

        tokens = tokenize(user_input)
        print("tokens ", tokens)
        if parenthesis_correct(tokens):
            instructions = translate(tokens)
            # instructions
            print("instr ",instructions)
            result = evaluate(instructions)
            print(f"lisp >> {result}")
        else:
            print(f"lisp >> Parenthesis Error")



if __name__ == '__main__':
    repl()