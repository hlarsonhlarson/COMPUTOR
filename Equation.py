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

    def set_abc(self):
        if 2 in self.coefficient_dict:
            a = self.coefficient_dict[2]
        else:
            a = 0
        if 1 in self.coefficient_dict:
            b = self.coefficient_dict[1]
        else:
            b = 0
        if 0 in self.coefficient_dict:
            c = self.coefficient_dict[0]
        else:
            c = 0
        return a,b,c

    def quadratic_solver(self, biggest_pow):
        a, b, c = self.set_abc()
        if biggest_pow == 2:
            D = b * b - 4 * a * c
            if D < 0:
                print('Discriminant is negative, can\'t solve in real numbers')
            else:
                x1 = -b + find_root(D, 2) / 2 / a
                x2 = -b - find_root(D, 2) / 2 / a
                if x1 == x2:
                    print(f'Discriminant is equal to zero. The solution is {x1}')
                else:
                    print(f'Discriminant is greater than zero. \nThe solutions are:\n{x1}\n{x2}')
        elif biggest_pow == 1:
            print(f'The solution is {-c/b}')
        else:
            print('There is no solution because it\'s something strange')

    def mega_solver(self):
        print('Stub')

    def find_biggest_pow(self):
        tmp = sorted(self.coefficient_dict.items(), key=lambda x: x[0], reverse=True)
        for key, value in tmp:
            if value:
                return key
        print('The solution is R')
        exit()

    def solve(self):
        biggest_pow = self.find_biggest_pow()
        print(f'Polynomial degree: {biggest_pow}')
        if biggest_pow < 3:
            self.quadratic_solver(biggest_pow)
        else:
            self.mega_solver
