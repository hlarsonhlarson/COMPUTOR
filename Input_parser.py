
def polish_notation(input_args):
    op_stack = []
    final_stack = []
    for elem in input_args:
        if elem.isdigit():
            final_stack.append(float(elem))
        elif elem.isalpha():
            final_stack.append(elem)
        else:
            op_stack.append(elem)
    return final_stack


def parse_input():
    input_string = input()
    input_string = input_string.lower()
    input_args = input_string.split()
    coefficient_dict = {}

    stack = polish_notation(input_args)

    return coefficient_dict


parse_input()

# test case 16 * X^0 + 15 + 1233 * X^1 - 24 + 41111 * X^1 - 5 * X^2 = 8 * X^3
# 16 * X^0 + 15 + 1233 * X^1 - 24 + 41111 * X^1 - 5 * X^2 - (8 * X^3) = 0
# use for equation
# if elem == '=':
#    elem = '-'
