from matplotlib.axes import Axes
from matplotlib.collections import QuadMesh
import numpy as np

class MandelbrotAxes(Axes):
    name = 'mandelbrot'
    
    def __init__(self, *args, **kwargs):
        #*args : Position Arguments
        #**kwargs : Keyword Arguments
        # ensures that the parent class's initialization code runs, allowing the class to properly inherit and initialize from its superclass.
        super().__init__(*args, **kwargs)
    
    def pcolormesh(
        self, 
        real_axis,
        imag_axis,
        alpha = None, 
        norm = None, 
        cmap = None, 
        vmin = None, 
        vmax = None, 
        shading = None, 
        antialiased = False, 
        data: np.ndarray | None = None,       
        attach_colorbar=True, 
        **kwargs,
    ) -> QuadMesh:

        if not isinstance(data, np.ndarray):
            raise TypeError("Invalid data, must be numpy array.")
        
        self.set_aspect("equal")
        self.tick_params(direction="in")

        self.set_xlabel("Real Axis")
        self.set_xlim(min(real_axis), max(real_axis))

        self.set_ylabel("Imaginary Axis")
        self.set_ylim(min(imag_axis), max(imag_axis))

        self.set_title("Mandelbrot Set")
        pcm_data = data
        pcm = super().pcolormesh(
            real_axis,
            imag_axis,
            pcm_data, 
            alpha = None, 
            norm = None, 
            cmap = cmap, 
            vmin = np.min(data), 
            vmax = np.max(data), 
            shading = None, 
            antialiased = False,  
            **kwargs,   
        )


        if pcm is None:
            raise RuntimeError("No colormesh generated.")
        if attach_colorbar:
            cb = self.figure.colorbar(pcm, ax=self, shrink=0.4, pad=0.02)
            cb.ax.tick_params(direction="in")
    
        return pcm
