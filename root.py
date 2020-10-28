def find_pow(num, degree):
    if degree == 0:
        return 1
    result = num
    for i in range(degree - 1):
        result *= num
    return result


def find_root(num, root_degree, eps=0.0000001):
    # Начальное приближение корня
    root = num / root_degree

    while abs(find_pow(root, root_degree) - num) >= eps:
        root = ((root_degree - 1) * root + num/find_pow(root,root_degree - 1)) / root_degree
    return root
