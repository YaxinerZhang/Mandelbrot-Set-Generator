import numpy as np
from ._mandelbrot_coloring_pyx import _Mandelbrot_ColoringAlgorithms_pyx

def _Mandelbrot_ColoringAlgorithms(real_axis, imag_axis, max_iters, radius):
    _real_axis = np.array(real_axis, dtype=np.float64)
    _imag_axis = np.array(imag_axis, dtype=np.float64)
    return np.asarray(_Mandelbrot_ColoringAlgorithms_pyx(_real_axis, _imag_axis, max_iters, radius))