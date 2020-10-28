from mpmath import mpf
from .degree import degree
from .External_root import external_root
from .Internal_root import internal_root
from .utils import sign, lc


def real_roots_from_derivative_roots(p, derivative_roots, solver, tolerance):
        """
        This function finds the real roots of polynomial p, using the roots of the derivative of p
        Parameters
        ----------
        p : dicts of coefficients of polynom
        derivative_roots : listList of all roots of p'. Must be in ascending order
        solver : functionA bracketing root-finding function such as bisection
        tolerance: mpmath number
            it's epsilon
        ----------
        """
        n_derivative_roots = len(derivative_roots)
        roots = []
        if n_derivative_roots == 0: # I took 0, but any point should work
            left_extremity = mpf(0)
            right_extremity = mpf(0)
        else:
            left_extremity = derivative_roots[0]
            right_extremity = derivative_roots[-1]
        right_limit_sign = sign(lc(p))  # LC: Leading Coefficient
        if degree(p) % 2 == 0:
            left_limit_sign = sign(lc(p))
        else:
            left_limit_sign = -sign(lc(p))
        roots = roots + external_root(p, left_extremity, left_limit_sign, mpf(-1), tolerance, solver)
        for i in range(n_derivative_roots - 1):
            roots = roots + internal_root(p,  derivative_roots[i], derivative_roots[i+1], tolerance, solver)
        roots = roots + external_root(p,  right_extremity,
                                      right_limit_sign, mpf(1), tolerance, solver)
        return roots
