import numpy as np
import matplotlib.pyplot as plt


def mandelbrot_set(max_iterations: int, magnitude_threshold: float, n: int) -> np.array:
    """
    Calculates a mandelbrot set.
    Calculated across x and y axes of -2 to 1 and -1 to 1, respectively.

    Parameters
    ----------
    max_iterations: int
        the maximum number of iteractions that are checked for escape.
    magnitude_threshold: float
        the magnitude, beyond which a sample in the set has escaped.
    n: int
        the number of x and y samples in the set.
    """
    x = np.linspace(-2.0, 1.0, n)
    y = np.linspace(-1.0, 1.0, n)
  
    c = x[: ,np.newaxis] +  (1j * y[np.newaxis,:])
    z = c
    escape_counts = x[: ,np.newaxis] +  y[np.newaxis,:]

    with np.warnings.catch_warnings():
        np.warnings.simplefilter("ignore")  # lotsa overflow

        for i in range(max_iterations): 
            z = z**2 + c
            escape_counts[abs(z) >= magnitude_threshold] = i + 1
    
    return escape_counts.T


if __name__ == "__main__":
    mandelbrot_img = mandelbrot_set(100, 100, 5000)
    plt.imshow(mandelbrot_img, cmap="plasma", extent=[-2.0, 1.0, -1.0, 1.0,])
    plt.show()
