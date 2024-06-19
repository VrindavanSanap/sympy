import sympy as sp
from sympy.vector import CoordSys3D, Del, curl
from sympy import *

delop = Del()
N = CoordSys3D('N')
x, y, z = N.x, N.y, N.z
i, j, k = N.i, N.j, N.k

init_printing()
"""
Use stokes theorem to rewrite line integral as
surface integral

 ∫(4yi + zcos(x)j - yk).dr
"""
# surface = (y * ln(z)) * i + (z - 2 * x) * k
surface = input()
surface = eval(surface)
print(f"Surface = {surface}")
print()
curl = eval(f"curl({surface})")
print()
print(f"Curl = {curl}")
print()
print(f"Negaitve curl = {-curl}")
