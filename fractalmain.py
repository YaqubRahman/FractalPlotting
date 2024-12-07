import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import math

def complex_matrix(xmin,xmax,ymin,ymax, pixel_density):
    re = np.linspace(xmin, xmax, int((xmax - xmin) * pixel_density))
    im = np.linspace(ymin, ymax, int((ymax - ymin) * pixel_density))
    return re[np.newaxis, :] + im[:, np.newaxis] * 1j


def is_stable(c, num_iterations):
    z = 0
    for _ in range(num_iterations):
        z = z ** 2 + c
    return abs(z) <= 2

#Turning boolean mask of stability into the initial complex numbers that seeded the sequence using Numpys masked filtering
#In simple terms - marking spots which are stable and unstable - and using the stable spots as our initial complex numbers
def get_members(c, num_iterations):
    mask = is_stable(c, num_iterations)
    return c[mask]


#matrix = complex_matrix(-1, 1, -1, 1, 10)
#print(matrix)
##stabletest = is_stable(5, 22)
##print(stabletest)

c = complex_matrix(-2, 0.5, -1.5, 1.5, pixel_density=800)
members = get_members(c, num_iterations=20)

plt.scatter(members.real, members.imag, color="black", marker=",", s=1)
plt.gca().set_aspect("equal")
plt.axis("off")
plt.tight_layout()
plt.show()