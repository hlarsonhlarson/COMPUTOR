from error import error


class Variable:

    def __init__(self, part):
        self.part = part
        self.prove_of_piece()
        self.pow = float(part[2:])
        self.letter = part[0]
        self.coeff = 1

    def prove_of_piece(self):
        if not ('^' in self.part):
            self.part = f'{self.part}^1'
        splitted_piece = self.part.split('^')
        if '' in splitted_piece:
            error(f'token "{self.part}" is not completed')
        if len(splitted_piece) != 2:
            error(f'very many symbols "^" in the token "{self.part}"')
        if not splitted_piece[0].isalpha():
            error(f'the token "{self.part}" must be contained a letter of the variable on the second position')
        if not splitted_piece[1].isdigit():
            error(f'the token "{self.part}" must be contained only an integer number on the second position')
        if int(splitted_piece[1]) < 0:
            error(
                f'the power "{splitted_piece[1]}" of the variable "{splitted_piece[0]}" in the token "{self.part}" is too little')

    def set_num_coef(self, num):
        self.coeff *= num

    def perfom_op(self, var2, op):
        if op == '*':
            self.coeff *= var2.coeff
            self.pow += var2.pow
        elif op == '/':
            self.coeff /= var2.coeff
            self.pow -= var2.pow
        else:
            error('Something went wrong')
