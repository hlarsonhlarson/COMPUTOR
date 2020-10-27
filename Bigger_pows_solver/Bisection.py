def bisection(a, b, tolerance, p_as_function, func_pdiff):
    p_a = p_as_function(a)
    p_b = p_as_function(b)
    m = (a + b) / 2
    p_m = p_as_function(m)
    progress = True
    iter = 0
    while abs(p_m) > tolerance and progress:
        iter += 1
        old_a, old_b = a, b
        if p_a * p_m <= 0:
            b = m
            p_b = p_m
        else:
            if p_b * p_m <= 0:
                a = m
                p_a = p_m
                m = (a + b) / 2
                p_m = p_as_function(m)
                if old_a == a and old_b == b:
                    progress = False
                    raise ValueError(f'bissection: no progress after {iter} iterations, ‘f‘with \na = {a} \nb = {b}')
    return m