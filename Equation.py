from Number import is_number, Number
from Variable import Variable
from Sign import Sign
from error import error


class Equation:
    def __init__(self, stack):
        self.stack = stack
