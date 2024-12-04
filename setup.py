from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy

extensions = [
    Extension(
        'mandelbrotpy._mandelbrot_iter_pyx',
        sources=['mandelbrotpy/_mandelbrot_iter.pyx'],
        include_dirs=[numpy.get_include()]  # Make sure numpy headers are included
    ),
    Extension(
        'mandelbrotpy._mandelbrot_escapetime_pyx',
        sources=['mandelbrotpy/_mandelbrot_escapetime.pyx'],
        include_dirs=[numpy.get_include()]  # Make sure numpy headers are included
    ),
    Extension(
        'mandelbrotpy._mandelbrot_coloring_pyx',
        sources=['mandelbrotpy/_mandelbrot_coloring.pyx'],
        include_dirs=[numpy.get_include()]  # Make sure numpy headers are included
    ),

]

setup(
    name="mandelbrotpy",
    ext_modules=cythonize(extensions),  # 传入扩展列表
    include_dirs=[numpy.get_include()]
)
