import numpy as np 

def _mandelbrot_iter_pyx(float complex c, int max_iters, float radius) -> int:
    """
    Mandelbrot function.

    Arguments
    ---------
    c: A complex number.
    max_iters: Max number of iterations.
    radius: Set a boundary for iterations.
    """
    cdef float complex z = 0
    cdef int n

    for n in range(max_iters):
        if abs(z) > radius:
            return n
        z = z * z + c
    return max_iters