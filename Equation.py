from Number import is_number, Number
from Variable import Variable
from Sign import Sign
from error import error


class Equation:
    def __init__(self, stack):
        self.stack = stack
        self.coefficient_dict = None

    def stack_pl_mi(self):
        self.stack = self.stack
        i = 0
        while i != len(self.stack):
            if isinstance(self.stack[i], Sign) and self.stack[i].sign in ['*', '/']:
                self.stack[i - 1].perfom_op(self.stack[i - 2], self.stack[i].sign)
                self.stack.remove(self.stack[i])
                self.stack.remove(self.stack[i - 2])
                i = i - 2
            i = i + 1
        self.stack = self.stack

    def set_coeff_dict(self):
        self.coefficient_dict = {}
        self.stack = self.stack
        self.coefficient_dict[self.stack[0].pow] = self.stack[0].coeff
        self.stack.remove(self.stack[0])
        i = 0
        while i != len(self.stack):
            if isinstance(self.stack[i], Sign) and self.stack[i].sign in ['+', '-']:
                if self.stack[i].sign == '+':
                    if self.stack[i - 1].pow in self.coefficient_dict:
                        self.coefficient_dict[self.stack[i - 1].pow] += self.stack[i - 1].coeff
                    else:
                        self.coefficient_dict[self.stack[i - 1].pow] = self.stack[i - 1].coeff
                else:
                    if self.stack[i - 1].pow in self.coefficient_dict:
                        self.coefficient_dict[self.stack[i - 1].pow] -= self.stack[i - 1].coeff
                    else:
                        self.coefficient_dict[self.stack[i - 1].pow] = -self.stack[i - 1].coeff
                self.stack.remove(self.stack[i])
                self.stack.remove(self.stack[i - 1])
                i = i - 2
            i = i + 1
