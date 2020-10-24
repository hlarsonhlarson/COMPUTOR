from preprocessing_string import parse_input
from Equation import Equation

input_string = "-1 * x^2 - 4 * x + 5 * x^1 = -5 * x^3 + 2"
output_stack = parse_input(input_string)
my_equation = Equation(output_stack)
my_equation.stack_pl_mi()
my_equation.set_coeff_dict()
print(my_equation.coefficient_dict)
