from .utils import p_as_function, diff_point


def newton(a, b, tolerance, p, maxiter=2000):
    # convergence not guaranteed
    iter = 0
    x_newton = (a + b)/2
    while abs(p_as_function(x_newton, p)) > tolerance:
        iter += 1
        if iter >= maxiter:
            raise ValueError(f'newton: no convergence after {iter} iterations')
            break
        x_newton = x_newton - p_as_function(x_newton, p)/diff_point(x_newton, p)
    return x_newton
