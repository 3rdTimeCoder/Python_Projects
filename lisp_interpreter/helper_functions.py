def add(operands):
    # print("add",operands)
    return sum(operands)


def equals(operands):
    # print("equals", operands)
    for i in range(operands.count('quote')):
        operands.remove('quote')
    return operands[0] == operands[1]


def car(operands):
    for i in range(operands.count("quote")):
        operands.remove("quote")
    if len(operands) != 0: return operands[0][0]
    else: return []


def cdr(operands):
    for i in range(operands.count("quote")):
        operands.remove("quote")
    if len(operands) != 0: return operands[0][1:]
    else: return []


def subtract(operands):
    # print("sub", operands)
    result = operands[0]
    for num in operands[1:]:
        result -= num
    return result


def divide(operands):
    # print("div",operands)
    result = operands[0]
    for num in operands[1:]:
        result /= num
    return result


def multiply(operands):
    # print("mul",operands)
    result = operands[0]
    for num in operands[1:]:
        result *= num
    return result


def is_atom(operands):
    if "quote" in operands: operands.remove('quote')
    if len(operands) > 1:
        return False
    return str(operands[0]).isalnum()


def quote(operands):
    for i in range(operands.count('quote')):
        operands.remove('quote')
    if (len(operands) == 1):
        return operands[0]
    return operands

def cons(operands):
    new_list = []
    for i in range(operands.count('quote')):
        operands.remove('quote')

    for element in operands:
        if isinstance(element, list):
            for list_element in element:
                new_list.append(list_element)
        else:
            new_list.append(element)

    return new_list


def cond(operands):
    print("cond", operands)
    true = [True, 't']

    for element in operands:
        if isinstance(element, list) and "quote" in element:
            element.remove("quote")
    print(operands)

    for lst in operands:
        if lst[0] in true:
            return lst[1]
    return []



if __name__ == '__main__':
    print(add(*[1,2,3,4,5])) 
    print(subtract(*[10,3,3,4])) 
    print(multiply(*[4,4])) 
    print(divide(*[4,4])) 
    print(car(*[10,3,3,4])) 
    print(cdr(*[10,3,3,4])) 
    print(is_atom(*[1,2,3,4]))
    
    