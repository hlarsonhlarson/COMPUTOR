def prepare_input_args(input_string):

    input_string = input_string.lower()
    input_args = input_string.split()

    equal_is_present = 0
    for i in range(len(input_args)):
        if input_args[i] == '=':
            input_args.remove(input_args[i])
            input_args.insert(i, '-')
            input_args.insert(i + 1, '(')
            input_args.append(')')
            equal_is_present = 1
            break
    return input_args, equal_is_present


def polish_notation(input_args):
    op_stack = []
    final_stack = []
    x_is_present = 0
    another_mistake = 0
    for elem in input_args:
        if elem.isdigit():
            final_stack.append(float(elem))
        elif elem == '(':
            op_stack.append(elem)
        elif elem == ')':
            temp = op_stack.pop()
            while op_stack and temp != '(':
                final_stack.append(temp)
                temp = op_stack.pop()
        elif elem == '+' or elem == '-':
            while op_stack and op_stack[-1] != '(':
                final_stack.append(op_stack.pop())
            op_stack.append(elem)
        elif elem == '*' or elem == '/':
            while op_stack and op_stack[-1] != '-' and op_stack[-1] != '+' and op_stack[-1] != '(':
                final_stack.append(op_stack.pop())
            op_stack.append(elem)
        elif elem[0] == 'x':
            final_stack.append(elem)
            x_is_present = 1
        else:
            another_mistake = 1
            break
    while op_stack:
        final_stack.append(op_stack.pop())
    return final_stack, x_is_present, another_mistake


def is_op(ch):
    if ch == '+' or ch == '-' or ch == '*' or ch == '/':
        return True
    return False


def plus_or_minus(ch):
    if ch == '+' or ch == '-':
        return True
    return False


def work_with_plus_minus(x, number, coefficient_dict, op):
    if x in coefficient_dict:
        if op == '+':
            coefficient_dict[x] += 1
        else:
            coefficient_dict[x] -= 1
    else:
        if op == '+':
            coefficient_dict[x] = 1
        else:
            coefficient_dict[x] = -1
    if 'x^0' in coefficient_dict:
        if op == '+':
            coefficient_dict['x^0'] += number
        else:
            coefficient_dict['x^0'] -= number
    else:
        if op == '+':
            coefficient_dict['x^0'] = number
        else:
            coefficient_dict['x^0'] = -number


def work_with_variable(x, number, coefficient_dict, op):
    if plus_or_minus(op):
        work_with_plus_minus(x, number, coefficient_dict, op)
        return
    if x in coefficient_dict:
        if op == '*':
            coefficient_dict[x] += number
        else:
            coefficient_dict[x] += 1 / number
    else:
        if op == '*':
            coefficient_dict[x] = number
        else:
            coefficient_dict[x] = 1 / number


def work_with_nums(num1, num2, coefficient_dict, op):

    result = 0
    if op == '*':
        result = num1 * num2
    elif op == '/':
        result = num1 / num2
    elif op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    if 'x^0' in coefficient_dict:
        coefficient_dict['x^0'] += result
    else:
        coefficient_dict['x^0'] = result


def work_with_variable_two(x, y, coefficient_dict, op):
    if op == '-':
        if y in coefficient_dict:
            coefficient_dict[y] *= -1
        else:
            coefficient_dict[y] = -1
    if x not in coefficient_dict:
        coefficient_dict[x] = 1


def polish_processing(stack):
    coefficient_dict = {}
    error = 0
    i = 0
    for i in range(len(stack)):
        print(i, len(stack), stack)
        print(coefficient_dict)
        if is_op(stack[i]):
            if isinstance(stack[i - 1], float) and isinstance(stack[i - 2], str):
                work_with_variable(stack[i - 2], stack[i - 1], coefficient_dict, stack[i])
                print('Hello1')
                print(stack[i - 2])
                print(stack[i - 1])
                print(coefficient_dict)
                print('Hiiiiiiiiiiii')
            elif isinstance(stack[i - 2], float) and isinstance(stack[i - 1], str):
                work_with_variable(stack[i - 1], stack[i - 2], coefficient_dict, stack[i])
                print('Hello2')
            elif isinstance(stack[i - 2], float) and isinstance(stack[i - 1], float):
                work_with_nums(stack[i - 2], stack[i - 1], coefficient_dict, stack[i])
                print('Hello3')
            elif isinstance(stack[i - 2], str) and isinstance(stack[i - 1], str):
                work_with_variable_two(stack[i - 2], stack[i-1], coefficient_dict, stack[i])
                print('Hello4')
            else:
                error = 1
                return coefficient_dict, error
            stack.remove(stack[i])
            i = i - 1
    return coefficient_dict, error


def parse_input():
    input_string = input()

    input_args, equal_is_present = prepare_input_args(input_string)

    stack, x_is_present, another_mistake = polish_notation(input_args)

    coefficient_dict, error = polish_processing(stack)

    print(coefficient_dict.keys())
    print('Hello')
    print(coefficient_dict)

    return coefficient_dict


parse_input()

# test case 16 * X^0 + 15 + 1233 * X^1 - 24 + 41111 * X^1 - 5 * X^2 = 8 * X^3
# 16 * X^0 + 15 + 1233 * X^1 - 24 + 41111 * X^1 - 5 * X^2 - (8 * X^3) = 0
# use for equation
# if elem == '=':
#    elem = '-'
