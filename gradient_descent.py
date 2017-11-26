#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt

def f(x):
	# Function
	return np.cos(x) - x

def f_(x):
	# Derivative of the function
	return - np.sin(x) - 1


def get_next_x(x):
	# Approximate a new x value using Newton's Method (Newton Raphson)
	return x - f_(x)

if __name__ == '__main__':
	X = np.linspace(-10, 10, 500, endpoint=True)
	F = f(X)

	# x0
	x = -6.

	# x values of iterations
	xs = []

	# Iteration count is specified
	# for _ in xrange(1,10):
	# 	xs.append(x)
	# 	x = get_next_x(x)

	# Threshold is specified
	while np.abs(f_(x)) > 0.01:
		xs.append(x)
		x = get_next_x(x)
	xs.append(x)

	# y values of iterations
	ys = f(xs)
	print(xs, ys)

	plt.plot(xs, ys, 'ro-')
	# First point represented in green color
	plt.plot(xs[0], ys[0], 'go')
	# Last point represented in blue color
	plt.plot(xs[-1], ys[-1], 'bo')

	plt.plot(X, F, 'k-')
	plt.grid(True)
	plt.show()
