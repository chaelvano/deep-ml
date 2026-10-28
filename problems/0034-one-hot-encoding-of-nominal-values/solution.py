import numpy as np

def to_categorical(x, n_col=None):
	# Your code here
	encoded = []

	if not n_col:
		n_col = 1 + x.max()

	for row in x:
		col = np.zeros(n_col)
		col[row] = 1.0

		encoded.append(col.tolist()) # appending np.array fails test case

	return encoded