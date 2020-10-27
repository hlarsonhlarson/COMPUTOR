from .degree import degree
from .Derivative import derivate
from .Real_root_from_derivative_roots import real_roots_from_derivative_roots
from .utils import find_low_coeffs


def mp_roots(p, solver):
    """
    Returns a list of all real roots of polynomial p.
    Parameters
    ----------
    p : dict of coefficients
    solver : functionA root-finding function such as bisection, newton, brent or hibrid
    ----------
    """
    todo = []  # to do stack
    while degree(p) > 1:  # push derivatives
        todo.append(p)
        p = derivate(p)
    # p is a first degree polynomial
    cfs = find_low_coeffs(p)
    roots = [(cfs[1]) / (cfs[0])]
    while len(todo) > 0: # pop derivatives
        derivative_roots = roots
        p = todo.pop()
        roots = real_roots_from_derivative_roots(p, derivative_roots, solver)
    return roots
