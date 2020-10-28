from .utils import p_as_function, diff_point
from parsing_string_utils.error import error


def hibrid( a, b, tolerance, p):
    """Solver that mixes Newton-Raphson and Bisection methods.
    Adapted from https://doi.org/10.12988/ams.2017.710302
    """
    iter = 0
    f_a = p_as_function(a, p)
    f_b = p_as_function(b, p)
    if f_a * f_b > 0:
        error(f'f(a) and f(b) must have opposite signs')
    n_bisec = 0
    n_newton = 0
    m = (a + b)/2
    f_m= p_as_function(m, p)
    while abs(f_m) > tolerance:
        old_a, old_b = a, b
        iter += 1
        f_m = p_as_function(m, p)
        fdiff_m = diff_point(m, p)
        next_x_newton = m - f_m / fdiff_m
        if a <= next_x_newton <= b:  # and (iter % 10 != 0):
            # Take newton guess
            m = next_x_newton
            n_newton += 1
        else:  # Take bisectionguess
            m = (a + b)/2
            n_bisec += 1
        f_m = p_as_function(m, p)
        if f_a * f_m <= 0:
            b = m
            f_b = f_m
        if f_b * f_m <= 0:
            a = m
            f_a = f_m
        if a == old_a and b == old_b:
            error(f'hibrid: no progress after {iter} iterations, ‘f’with b -a = {b -a}')
            break
    return m
