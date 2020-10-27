from parsing_string_utils.error import error
from root import find_pow
from .Derivative import derivate


def LC(coeff_dict: dict):
    tmp = coeff_dict.items()
    tmp = sorted(tmp, key=lambda x: x[0], reverse=True)
    for key, value in tmp:
        if value != 0:
            return value
    return 0


def sign(coeff_dict):
    tmp = coeff_dict.items()
    tmp = sorted(tmp, key=lambda x: x[0], reverse=True)
    for key, value in tmp:
        if value != 0:
            return 1 if value > 0 else 0
    return 0


def find_low_coeffs(coeff_dict: dict):
    print(coeff_dict)
    if 0 in coeff_dict:
        b = coeff_dict[0]
    else:
        error('Something bad')
        b = 0
    if 1 in coeff_dict:
        a = coeff_dict[0]
    else:
        a = 0
    return a, b


def p_as_function(num, coeff_dict):
    result = 0
    for key, value in coeff_dict.items():
        result += value * find_pow(num, key)
    return result


def diff_point(point, coeff_dict):
    derivate_dict = derivate(coeff_dict)
    return p_as_function(point, derivate_dict)
