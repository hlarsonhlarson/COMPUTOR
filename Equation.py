from Number import is_number, Number
from Variable import Variable
from Sign import Sign
from error import error
from _collections import defaultdict
from EquationPart import EquationPart
from root import find_root


class Equation:
    def __init__(self, stack):
        self.stack = stack
        self.coefficient_dict = None

    def stack_pl_mi(self):
        i = 0
        while i != len(self.stack):
            if isinstance(self.stack[i], Sign) and self.stack[i].sign in ['*', '/']:
                self.stack[i - 1].perfom_op(self.stack[i - 2], self.stack[i].sign)
                self.stack.remove(self.stack[i])
                self.stack.remove(self.stack[i - 2])
                i = i - 2
            i = i + 1

    def set_coeff_dict(self):
        i = 0
        while i != len(self.stack):
            if isinstance(self.stack[i], Sign) and self.stack[i].sign in ['+', '-']:
                if self.stack[i].sign == '+':
                    tmp_res = self.stack[i - 2].plus(self.stack[i - 1])
                else:
                    tmp_res = self.stack[i - 2].minus(self.stack[i - 1])
                self.stack.remove(self.stack[i])
                self.stack.remove(self.stack[i - 1])
                self.stack.remove(self.stack[i - 2])
                i = i - 3
                self.stack.insert(i + 1, tmp_res)
            i = i + 1
        self.coefficient_dict = self.stack[0].coeff_dict

    def simple_form(self):
        output_string = ''
        tmp_dict = self.coefficient_dict.items()
        tmp_dict = sorted(tmp_dict, key=lambda x: x[0])
        for key, value in tmp_dict:
            if value < 0:
                output_string = output_string[:-2]
                output_string = output_string + '- '
                value *= -1
            output_string += f'{value} * X^{key} + '
        output_string = output_string[:-2]
        output_string += '= 0'

    def solve(self):
        print(find_root(8, 3))
