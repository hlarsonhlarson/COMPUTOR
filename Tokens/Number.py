from parsing_string_utils.error import error


def is_number(part):
    if part == '':
        return False
    if part[0] == '-' and len(part) > 1:
        part = part[1:]
    if part.isdigit():
        return True
    splitted_part = part.split('.')
    if '' in splitted_part or len(splitted_part) != 2:
        return False
    return True


class Number:

    def __init__(self, part):
        self.part = part
        self.check_piece()
        self.num = float(self.part)

    def check_piece(self):
        if is_number(self.part):
            return
        if '.' not in self.part:
            error(f'"{self.part}" is not valid')
        splitted_piece = self.part.split('.')
        if '' in splitted_piece:
            error(f'"{self.part}" is not completed')
        count_of_dots = 0
        count_of_numbers = 0
        for sign in self.part:
            if sign == '.':
                count_of_dots += 1
            elif sign.isdigit():
                count_of_numbers += 1
            else:
                error(f'unidentified letter "{sign}" in the token "{self.part}"')
        if count_of_dots != 1:
            error(f'very many dots in the token "{self.part}"')
