from Number import is_number, Number
from Variable import Variable
from Sign import Sign
from error import error


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
        if is_number(elem):
            final_stack.append((elem))
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


def get_token_class(piece_of_string):
    if is_number(piece_of_string):
        tmp_num = Number(piece_of_string)
        tmp_num.check_piece()
        tmp_var = Variable('x^0')
        tmp_var.set_num_coef(tmp_num.num)
        return tmp_var
    elif '^' in piece_of_string:
        return Variable(piece_of_string)
    elif len(piece_of_string) == 1 and piece_of_string.isalpha():
        return Variable(piece_of_string + '^1')
    elif piece_of_string in ('+', '-', '*', '/'):
        return Sign(piece_of_string)
    error(f'unidentified token {piece_of_string}')


def preprocess_stack(stack):
    processed_stack = []
    for elem in stack:
        token = get_token_class(elem)
        processed_stack.append(token)
    return processed_stack


def parse_input(input_string):

    input_args, equal_is_present = prepare_input_args(input_string)

    stack, x_is_present, another_mistake = polish_notation(input_args)

    print(stack)

    output_stack = preprocess_stack(stack)

    return output_stack



# test case 16 * X^0 + 15 + 1233 * X^1 - 24 + 41111 * X^1 - 5 * X^2 = 8 * X^3
# 16 * X^0 + 15 + 1233 * X^1 - 24 + 41111 * X^1 - 5 * X^2 - (8 * X^3) = 0
# use for equation
# if elem == '=':
#    elem = '-'
