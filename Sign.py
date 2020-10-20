from error import error


class Sign:
    def __init__(self, part):
        self.sign = part
        self.check_piece()

    def check_piece(self):
        if self.sign not in ['+', '*', '/', '-']:
            error(f'"{self.sign} is invalid')
