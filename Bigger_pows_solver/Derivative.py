def derivate(coef_dict: dict):
    tmp_dict = {}
    for key, value in coef_dict.items():
        tmp_dict[key - 1] = value * key
    return tmp_dict
