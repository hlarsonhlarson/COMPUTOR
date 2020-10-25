from preprocessing_string import parse_input
from Equation import Equation

input_string = "6 * x^0 + x + 0 * x^3 = 2"
output_stack = parse_input(input_string)
my_equation = Equation(output_stack)
my_equation.stack_pl_mi()
my_equation.set_coeff_dict()
my_equation.simple_form()
my_equation.solve()
