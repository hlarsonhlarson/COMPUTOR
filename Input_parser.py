def prepare_input_args(input_string):

    input_string = input_string.lower()
    input_args = input_string.split()

    equal_is_present = 0
    for i in range(len(input_args)):
        if input_args[i] == '=':
            input_args.remove(input_args[i])
            input_args.insert(i - 1, '-')
            input_args.insert(i, '(')
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


def polish_processing(stack):
    coefficient_dict = {}
    for i in range(len(stack)):
        if stack[i] == '*' or stack[i] == '/' or stack[i] == '+' or stack[i] == '-':
            if stack[i-1].isdigit() and  not stack[i -2].isdigit():
                if stack[i - 2] in coefficient_dict:
                    coefficient_dict[stack[i - 2]] = stack[i - 1]
                 else:
                   coefficient_dict[stack[i - 2]] += stack[i - 1]
            elif stack[i - 2].isdigit() and not stack[i - 1].isdigit():
                if stack[i - 1] in coefficient_dict:
                    coefficient_dict[stack[i - 1]] = stack[i - 2]
                else:
                    coefficient_dict[stack[i - 1]] += stack[i - 2]
    return coefficient_dict


def parse_input():
    input_string = input()

    input_args, equal_is_present = prepare_input_args(input_string)

    stack, x_is_present, another_mistake = polish_notation(input_args)

    coefficient_dict = polish_processing(stack)

    return coefficient_dict


parse_input()

# test case 16 * X^0 + 15 + 1233 * X^1 - 24 + 41111 * X^1 - 5 * X^2 = 8 * X^3
# 16 * X^0 + 15 + 1233 * X^1 - 24 + 41111 * X^1 - 5 * X^2 - (8 * X^3) = 0
# use for equation
# if elem == '=':
#    elem = '-'
