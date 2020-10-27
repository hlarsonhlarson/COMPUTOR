def degree(coeff_dict: dict):
    tmp = coeff_dict.items()
    tmp = sorted(tmp, key=lambda x: x[0], reverse=True)
    for key, value in tmp:
        if value != 0:
            return key
    return 0
