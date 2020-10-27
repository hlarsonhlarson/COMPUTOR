def mpmath_solver ( a, b, tol, f, func_pdiff):
    return findroot(f, (a + b)/mpf(2), solver='anewton', tol = tol, maxsteps = 10000)