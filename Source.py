import matplotlib.pyplot as plt
import numpy as np


def midpoint_displacement(xl, yl, xr, yr, roughness, eps):
    def displace(midpoint, length, roughness):
        return midpoint + roughness * length * (np.random.rand() * 2 - 1)

    def subdivide(xl, yl, xr, yr, roughness, eps, points):
        xm = (xl + xr) / 2
        ym = (yl + yr) / 2

        length = np.abs(xr - xl)
        ym = displace(ym, length, roughness)

        if length < eps:
            points.append((xr, yr))
            return

        subdivide(xl, yl, xm, ym, roughness, eps, points)
        subdivide(xm, ym, xr, yr, roughness, eps, points)

    points = [(xl, yl)]
    subdivide(xl, yl, xr, yr, roughness, eps, points)
    points.append((xr, yr))

    return points

xl, yl = -10, 0
xr, yr = 10, 0
roughness = 0.8
eps = 0.005

points = midpoint_displacement(xl, yl, xr, yr, roughness, eps)


x_coords, y_coords = zip(*points)
plt.figure(figsize=(16, 9))
plt.axis("equal")
plt.plot(x_coords, y_coords, 'black')

plt.xlim(-10,10)
plt.ylim(-10,10)
plt.show()