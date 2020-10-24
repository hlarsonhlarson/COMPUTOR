from Variable import Variable


class Equation_part:
    def __init__(self, coeff_dict):
        self.coeff_dict = coeff_dict

    def plus_variable(self, b):
        if b.pow in self.coeff_dict:
            self.coeff_dict[b.pow] += b.coeff
        else:
            self.coeff_dict[b.pow] = b.coeff
        return self

    def plus(self, b):
        if isinstance(b, Variable):
            return self.plus_variable(b)
        for key, value in b.coeff_dict.items():
            if key in self.coeff_dict:
                self.coeff_dict[key] += value
            else:
                self.coeff_dict[key] = value
        return self

    def minus(self, b):
        if isinstance(b, Variable):
            b.coeff *= -1
            return self.plus_variable(b)
        for key, value in b.coeff_dict.items():
            if key in self.coeff_dict:
                self.coeff_dict[key] -= value
            else:
                self.coeff_dict[key] = -value
        return self

    def invert_minus(self, b):
        for key, value in self.coeff_dict:
            self.coeff_dict[key] = -value
        return self.plus_variable(b)
