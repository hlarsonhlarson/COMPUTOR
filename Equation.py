from Number import is_number, Number
from Variable import Variable
from Sign import Sign
from error import error


class Equation:
    def __init__(self, stack):
        self.stack = stack
        self.coefficient_dict = None

    def fill_coeff_dict(self):
        tmp_stack = self.stack
        for i in range(len(tmp_stack)):
            if tmp_stack[i] is Sign:
                tmp_result = tmp_stack[i - 1].perfom_op(tmp_stack[i - 2], tmp_stack[i])

