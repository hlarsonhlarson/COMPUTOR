from .utils import sign, p_as_function


def internal_root(p, a, b, tolerance, solver):
    """Looks for a root in intervals where both limits are finite numbers
    Parameters
    ----------
    p : coeff dict
    a : number
        Left limit of interval
    b : number
        Right limit of interval
    tolerance : mpmath mpf number
        A number x is considered a root of p if abs(p(x)) < tolerance
    solver : functionA bracketing root-finding function such as bisection
    ----------
    """
    p_a = p_as_function(a, p)
    if abs(p_a) <= tolerance:
        root_found = []
    else:
        p_b = p_as_function(b, p)
        if abs(p_b) < tolerance:
            root_found = [b]
        else:
            sign_at_a = sign(p_a)
            sign_at_b = sign(p_b)
            if sign_at_a == sign_at_b:
                root_found = []
            else:
                root_found = [solver(a, b, tolerance, p)]
    return root_found
