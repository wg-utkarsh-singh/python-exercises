from math import pi


def vol(h, r=10):
    v = ((4 * pi * r**3) / 3) - (pi * h**2 * (3 * r - h) / 3)
    return v


print(vol(2))
