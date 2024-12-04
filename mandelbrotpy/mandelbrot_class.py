from ._mandelbrot_escapetime import _Mandelbrot_EscapeTimeAlgorithms
from ._mandelbrot_coloring import _Mandelbrot_ColoringAlgorithms


class MandelbrotSet:
    def __init__(self, max_iters: int, radius):
        """
        Initialize the Mandelbrot set parameters.

        Arguments:
        ----------
        max_iters: Maximum number of iterations.
        radius: Boundary for iterations.
        """
     
        self.max_iters = max_iters 
        self.radius = radius

    def get_mandelbrot(self, real_axis, imag_axis, option="EscapeTime"):
        """
        Compute mandelbrot set

        Parameters
        ----------
        real_axis: A real numpy array representing x-axis.
        imag_axis: A real numpy array representing y-axis.
        options: Algorithms to choose from.
        """
        match option:
            case "EscapeTime":
                return _Mandelbrot_EscapeTimeAlgorithms(real_axis, imag_axis, self.max_iters, self.radius)
            case "Coloring":
                return _Mandelbrot_ColoringAlgorithms(real_axis, imag_axis, self.max_iters, self.radius)
            case _:
                raise TypeError("Invalid option.")