from .Point_with_sign_inversion import point_with_sign_inversion
from .utils import p_as_function, sign


def external_root(p, extremity, limit_sign, initial_step, tolerance, solver):
    """
    Look for a root in intervals where one of its limits is -infinity or infinity
    Parameters
    ----------
    p : coefficients dict
    extremity : numberInterval is either (-infinity, extremity] or (extremity, infinity), depending on initial_step
    limit_sign :number sign
        Sign of polynomial at -infinity or at infinity, depending on initial_step
    initial_step :number
        initial_step must be a nonzero value; normally, initial_step == mpf(1). 
        If initial_step < 0, the function willstart by looking for a bracketing
        interval testing values from extremity towards -infinity.
        If initial_step > 0, the function will start by looking for a bracketing
        interval testing values from extremity towards infinity.
    tolerance : mpmath mpf number
        A number x is considered a root of p if abs(p(x)) < tolerance
    solver : function
        A bracketing root-finding function such as bisection
    ----------
    """
    value_at_extremity = p_as_function(extremity, p)
    if abs(value_at_extremity) <= tolerance:
        if initial_step < 0:
            root_found = [extremity]
        else:
            root_found = []
    else:
        sign_at_extremity = sign(value_at_extremity)
        if limit_sign == sign_at_extremity:
            root_found = []
        else:
            if initial_step > 0:
                a = extremity
                b = point_with_sign_inversion(extremity, sign_at_extremity, initial_step)
            else:
                a = point_with_sign_inversion(extremity, sign_at_extremity, initial_step)
                b = extremity
            root_found = [solver(a, b, tolerance, p)]
    return root_found
