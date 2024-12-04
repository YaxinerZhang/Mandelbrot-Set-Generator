import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Local
from mandelbrotpy import MandelbrotSet

def test_mandelbrot():
    print("Test mandelbrot plot.")
    lower, upper = (-2.0, -1.5), (0.75, 1.5)
    num_grids = (1000, 1000)
    max_iters = 100
    radius = 2.0 

    axes = [np.linspace(l, u, n) for l, u, n in zip(lower, upper, num_grids)]
    
    output_dir = Path("./.temp")
    output_dir.mkdir(exist_ok=True)  #ensure the dir is exist
    output_file = output_dir / "mandelbrot.png"

    real_axis = np.linspace(lower[0], upper[0], num_grids[0])
    imag_axis = np.linspace(lower[1], upper[1], num_grids[1])

    mandelbrot = MandelbrotSet(max_iters, radius)
    mandelbort_img_es = mandelbrot.get_mandelbrot(real_axis, imag_axis, option = "EscapeTime")
    mandelbort_img_co = mandelbrot.get_mandelbrot(real_axis, imag_axis, option = "Coloring")
    
    fig = plt.figure(figsize=(9, 8))
    ax1 = fig.add_subplot(1, 2, 1,  projection="mandelbrot")
    ax2 = fig.add_subplot(1, 2, 2,  projection="mandelbrot")
    ax1.pcolormesh(real_axis, imag_axis, data=mandelbort_img_es)
    ax2.pcolormesh(real_axis, imag_axis, data=mandelbort_img_co, cmap="coolwarm")

    plt.tight_layout()
    plt.savefig(output_file)
    print("Test succeeded.")


def test_mandelbrot_animation():
    print("Test mandelbrot animation.")
    output_dir = Path("./.temp")
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / "mandelbrot.html"

    c = [-0.75, 0.0]    #center
    num_grids = (1000, 1000)
    max_iters = 1000
    radius = 2.0 

    mandelbrot = MandelbrotSet(max_iters, radius)
    fig = plt.figure(figsize=(5.5, 5))
    ax = fig.add_subplot(projection="mandelbrot")

    def update(i):
        """Update frame."""
        print("Updating frame: {}...".format(i))
        ax.cla()   #clean the current ax
        r = 2.0 - i * 0.05
        r_min, r_max = c[0] - r, c[0] + r
        i_min, i_max = c[1] - r, c[1] + r
        real_axis = np.linspace(r_min, r_max, num_grids[0])
        imag_axis = np.linspace(i_min, i_max, num_grids[1])
        mandelbrot_data = mandelbrot.get_mandelbrot(real_axis, imag_axis, option="Coloring")
        pcm = ax.pcolormesh(real_axis, imag_axis, data=mandelbrot_data, attach_colorbar=False, cmap="coolwarm")
        return pcm, None

    ani = animation.FuncAnimation(fig=fig, func=update, frames=40, interval=30)
    ani.save(filename=output_file, writer="html")
    print("Test succeeded.")
