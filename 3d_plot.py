#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

def f(X,Y):
	# Function
	return X**3 - 3*X*Y + Y**3

# 3D
X = np.arange(-3., 3., .05)
Y = np.arange(-3., 3., .05)
X, Y = np.meshgrid(X, Y)

fig = plt.figure()
ax = Axes3D(fig)

ax.plot_surface(X,Y, f(X,Y),cmap=cm.coolwarm, linewidth=0, alpha=0.2, antialiased=False)
ax.hold(True)

# (1,1) is a local minimum of f(X,Y)
ax.scatter(1,1, f(1,1), c='r', s=100)
# (0,0) is a saddle point of f(X,Y)
ax.scatter(0,0, f(0,0), c='g', s=100)


plt.ylabel('X')
plt.ylabel('Y')
plt.show()
