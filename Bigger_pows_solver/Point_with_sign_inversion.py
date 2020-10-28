from .utils import sign, p_as_function


def point_with_sign_inversion(p: dict, extremity, sign_at_extremity, initial_step):
    """Finds a bracketing interval starting from an interval with one of its limits equal to infinity or -infinity
    Parameters
    ----------
    p: coeff dict of polynom
    extremity : number
        Interval is either (-infinity, extremity] or (extremity, infinity),
        and extremity is either the smallest or the greatest root of derivative,
        depending on initial_step.
    sign_at_extremity : number sign
        Sign of p(extremity)
    initial_step :
        number
        initial_step must be a nonzero value; normally, initial_step == mpf(1).
        If initial_step< 0, the function will start by looking for a bracketing
        interval testing values from extremity towards -infinity.
        If initial_step > 0, the function will start by looking for a bracketing
        interval testing values from extremity towards infinity.
    ----------
    """
    step = initial_step
    x = extremity + step
    p_x = p_as_function(x, p)
    sign_at_x = sign(p_x)
    while sign_at_x == sign_at_extremity:
        step = 2*step  # Double step length
        x = x + step
        p_x = p_as_function(x, p)
        sign_at_x = sign(p_x)
    return x
