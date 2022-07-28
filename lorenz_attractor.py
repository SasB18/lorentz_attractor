"""
Solves the Lorenz attractor
"""

import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

# declare initial values
# initial values are: sigma = 10, rho = 28, beta = 8/3
sigma = 10
rho = 28
beta = 8/3

x, y, z = 1, 1, 1

X0 = [x, y, z]

t = np.linspace(1, 50, 2000)

# define model
def attractor(N, t):
    """
    Defines the model of the lorenz attractor
    """
    x, y, z = N

    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x*y - beta*z

    return [dxdt, dydt, dzdt]

# solve the system of differential equations
solution = integrate.odeint(attractor, X0, t)

x, y, z = solution.T

# plotting
fig = plt.figure()
ax = plt.axes(projection="3d")

plt.title("Lorenz attractor")
ax.plot(x, y, z)

plt.show()