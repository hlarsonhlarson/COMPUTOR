def parse_input():
    input_string = input()
    input_string = input_string.lower().replace(' ', '')
    letters_nums = list(enumerate(input_string))
    coefficient_dict = {}

    x_place = [x for x, y in enumerate(input_string) if y == 'x']
    equality_place = [x for x, y in enumerate(input_string) if y == '=']
    return coefficient_dict


parse_input()
