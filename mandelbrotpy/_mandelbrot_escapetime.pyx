import numpy as np
cimport numpy as cnp
from ._mandelbrot_iter_pyx import _mandelbrot_iter_pyx
cnp.import_array()

def _Mandelbrot_EscapeTimeAlgorithms_pyx(cnp.float64_t[:] real_axis, cnp.float64_t[:] imag_axis, int max_iters, float radius):
    """
    Generate the Mandelbrot set.

    Returns:
    --------
     A 2D array representing the Mandelbrot set.
    """
    cdef int ni = imag_axis.shape[0]
    cdef int nj = real_axis.shape[0]
    cdef cnp.int32_t[:, :] res = np.zeros((ni, nj), dtype=np.int32)  # Use np.zeros instead of cnp.zeros
    cdef cnp.float64_t[:, :] res1 = np.zeros((ni, nj), dtype=np.float64)  # Use np.zeros instead of cnp.zeros
    cdef int i, j
    for j in range(nj):
        for i in range(ni):
            res[j, i] = _mandelbrot_iter_pyx(real_axis[i] + 1j * imag_axis[j], max_iters, radius)
            res1[j, i] = np.log10(res[j, i])
    return res1

