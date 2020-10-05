import re


def parse_input():
    input_string = input()
    input_string = input_string.lower().replace(' ', '')
    coefficient_dict = {}

    x_place = [x for x, y in enumerate(input_string) if y == 'x']
    equality_place = [x for x, y in enumerate(input_string) if y == '=']
    newstr = ''.join((ch if ch in '0123456789.-e' else ' ') for ch in input_string)
    newstr = re.split(r'(-)', newstr)
    # nums = [elem.split() for elem in newstr]
    # print(nums)
    print(newstr)




    return coefficient_dict


parse_input()
