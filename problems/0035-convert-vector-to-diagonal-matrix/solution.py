import numpy as np

def make_diagonal(x):
	# Your code here
	# return np.diag(x)

	return [[x[i] if i == j else 0 for j in range(len(x))] for i in range(len(x))]