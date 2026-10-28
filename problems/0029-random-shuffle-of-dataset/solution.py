import numpy as np

def shuffle_data(X, y, seed=None):
	# Your code here
	if seed:
		np.random.seed(seed)

	idx = np.random.permutation(len(X))

	return (X[idx], y[idx])