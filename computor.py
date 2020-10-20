from preprocessing_string import parse_input
from Equation import Equation

# input_string = input()
input_string = '-1 * x^2 + 1 = -2'
output_stack = parse_input(input_string)
print(output_stack)
my_equation = Equation(output_stack)