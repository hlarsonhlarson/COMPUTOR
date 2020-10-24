import Variable


class EquationPart:
    def __init__(self, coeff_dict):
        self.coeff_dict = coeff_dict

    def plus_variable(self, b):
        if b.pow in self.coeff_dict:
            self.coeff_dict[b.pow] += b.coeff
        else:
            self.coeff_dict[b.pow] = b.coeff
        return self

    def plus(self, b):
        if isinstance(b, Variable.Variable):
            return self.plus_variable(b)
        for key, value in b.coeff_dict.items():
            if key in self.coeff_dict:
                self.coeff_dict[key] += value
            else:
                self.coeff_dict[key] = value
        return self

    def minus(self, b):
        if isinstance(b, Variable.Variable):
            b.coeff *= -1
            return self.plus_variable(b)
        for key, value in b.coeff_dict.items():
            if key in self.coeff_dict:
                self.coeff_dict[key] -= value
            else:
                self.coeff_dict[key] = -value
        return self

    def invert_minus(self, b):
        for key, value in self.coeff_dict.items():
            self.coeff_dict[key] = -value
        return self.plus_variable(b)
