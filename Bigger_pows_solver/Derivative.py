def derivate(coeff_dict: dict):
    tmp_dict = {}
    for key, value in coeff_dict.items():
        tmp_dict[key - 1] = value * key
    return tmp_dict
