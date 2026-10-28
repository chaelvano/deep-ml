import numpy as np

def batch_iterator(X, y=None, batch_size=64):
	# Your code here
	batches = np.array_split(X, (len(X) + batch_size - 1) // batch_size)

	if y is not None:
		for i in range(len(batches)):
			batches[i] = [batches[i], y[i * batch_size:(1 + i) * batch_size]]

	return batches