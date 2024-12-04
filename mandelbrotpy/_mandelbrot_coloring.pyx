import numpy as np
cimport numpy as cnp
from ._mandelbrot_iter_pyx import _mandelbrot_iter_pyx

def _Mandelbrot_ColoringAlgorithms_pyx(cnp.float64_t[:] real_axis, cnp.float64_t[:] imag_axis, int max_iters, float radius):
    """
    Generate the Mandelbrot set with coloring algorithm.

    Returns:
    --------
     A 2D array representing the colored Mandelbrot set.
    """
    cdef int ni = imag_axis.shape[0]
    cdef int nj = real_axis.shape[0]
    cdef cnp.int32_t[:, :] res = np.zeros((ni, nj), dtype=np.int32)  # Use np.zeros instead of cnp.zeros
    cdef cnp.float64_t[:, :] hue = np.zeros((ni, nj), dtype=np.float64)  # Use np.zeros instead of cnp.zeros
    cdef cnp.int32_t[:] NumIterationsPerPixel = np.zeros(max_iters + 1, dtype=np.int32)  # Use np.zeros
    cdef int i, j, k, iter

    for j in range(nj):
        for i in range(ni):
            res[j, i] = _mandelbrot_iter_pyx(real_axis[i] + 1j * imag_axis[j], max_iters, radius)
            NumIterationsPerPixel[res[j, i]] += 1  # Fix variable name: use res[j, i] instead of undefined iteration
    
    cdef int total = 0
    for i in range(max_iters):
        total += NumIterationsPerPixel[i]
        
    for j in range(nj):
        for i in range(ni):
            iter = res[j, i]
            for k in range(iter):
                hue[j, i] += NumIterationsPerPixel[k] / total
    return hue

