from Number import is_number, Number
from Variable import Variable
from Sign import Sign
from error import error
from _collections import defaultdict
from Equation_part import Equation_part


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

    def pre_coeff_dict(self):
        i = 0
        while i != len(self.stack):
            print('HI')
            tmp_dict = defaultdict()
            if isinstance(self.stack[i], Sign) and self.stack[i].sign in ['+', '-']:
                if isinstance(self.stack[i - 1], Variable) and isinstance(self.stack[i - 2], Variable):
                    if self.stack[i].sign == '+':
                        tmp_dict[self.stack[i - 1].pow] = tmp_dict[self.stack[i - 1].pow] + self.stack[i - 1].coeff
                        tmp_dict[self.stack[i - 2].pow] = tmp_dict[self.stack[i - 2].pow] + self.stack[i - 2].coeff
                    else:
                        tmp_dict[self.stack[i - 1].pow] = tmp_dict[self.stack[i - 1].pow] - self.stack[i - 1].coeff
                        tmp_dict[self.stack[i - 2].pow] = tmp_dict[self.stack[i - 2].pow] - self.stack[i - 2].coeff
                    self.stack.remove(self.stack[i])
                    self.stack.remove(self.stack[i])
                    self.stack.remove(self.stack[i])
                    print(self.stack)
                    self.stack = Equation_part(tmp_dict) + self.stack
                    print(self.stack)
                    i = i - 3
            i = i + 1

    def set_coeff_dict(self):
        i = 0
        while i != len(self.stack):
            if isinstance(self.stack[i], Sign) and self.stack[i].sign in ['+', '-']:
                if self.stack[i].sign == '+':
                    tmp_res = self.stack[i - 1].plus(self.stack[i - 2])
                else:
                    tmp_res = self.stack[i - 1].minus(self.stack[i - 2])
                self.stack.remove(self.stack[i])
                self.stack.remove(self.stack[i])
                self.stack.remove(self.stack[i])
                self.stack = self.stack + [tmp_res]
                i = i - 3
            i = i + 1
        print(self.stack)
        self.coefficient_dict = self.stack[0].coefficient_dict
