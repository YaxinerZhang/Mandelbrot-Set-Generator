from matplotlib.projections import register_projection
from .mandelbrot_class import MandelbrotSet
from .mandelbrot_plot import MandelbrotAxes

register_projection(MandelbrotAxes)
