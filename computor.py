from parsing_string_utils.preprocessing_string import parse_input
from Tokens.Equation import Equation
from sys import argv

if __name__ == '__main__':
    if len(argv) != 2:
        print('Incorrect input. Usage: python3 computor.py "{your expression}"')
        exit(1)
    input_string = argv[1]
    output_stack = parse_input(input_string)
    my_equation = Equation(output_stack)
    my_equation.stack_pl_mi()
    my_equation.set_coeff_dict()
    my_equation.simple_form()
    my_equation.solve()
