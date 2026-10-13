import matplotlib.pyplot as plt
import numpy as np

def mandelbrot(h, w, maxit=20, r=20):
    x = np.linspace(-2.5, 1.5, 4*h+1)
    y = np.linspace(-1.5, 2.5, 4*w+1)
    A, B = np.meshgrid(x, y)
    C = A + B*1j
    z = np.zeros_like(C)
    divtime = maxit + np.zeros(z.shape, dtype=np.int_)

    for i in range(maxit):
        z = z**2 + C
        diverge = abs(z) > r
        div_now = diverge & (divtime == maxit)
        divtime[div_now] = i
        z[diverge] = r
         
    return divtime

if __name__ == "__main__":
    plt.figure(figsize=(8, 8))
    plt.imshow(mandelbrot(400, 400), cmap='twilight_shifted')
    plt.axis('off')  # Hide axes ticks
    plt.show()

