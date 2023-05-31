def add(*args):
    print("args ", args)
    return sum(args)


def equals(*args):
    args_list = list(args)
    for i in range(args_list.count('quote')):
        args_list.remove('quote')
    print(args_list)
    return args_list[0] == args_list[1]


def car(*args):
    return args[0]


def cdr(*args):
    return list(args[1:])


def subtract(*args):
    result = args[0]
    for num in args[1:]:
        result -= num
    return result


def divide(*args):
    result = args[0]
    for num in args[1:]:
        result /= num
    return result


def multiply(*args):
    result = args[0]
    for num in args[1:]:
        result *= num
    return result


def is_atom(*args):
    args_list = list(args)
    args_list.remove('quote')
    if len(args_list) > 1:
        return False
    return str(args[0]).isalnum()


def quote(*args):
    return args[0]

def cons(*args):
    pass



if __name__ == '__main__':
    print(add(*[1,2,3,4,5])) 
    print(subtract(*[10,3,3,4])) 
    print(multiply(*[4,4])) 
    print(divide(*[4,4])) 
    print(car(*[10,3,3,4])) 
    print(cdr(*[10,3,3,4])) 
    print(is_atom(*[1,2,3,4]))
    
    