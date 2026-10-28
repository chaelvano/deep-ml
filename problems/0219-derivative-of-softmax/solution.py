import numpy as np

def softmax_derivative(x: list[float]) -> list[list[float]]:
	"""
	Compute the Jacobian matrix of the softmax function.
	
	Args:
		x: Input vector of real numbers
		
	Returns:
		Jacobian matrix J where J[i][j] = d(softmax_i)/d(x_j)
	"""
	# Your code here
	x = np.array(x)

	p = np.exp(x - x.max()) / sum(np.exp(x - x.max()))

	return np.diag(p) - np.outer(p, p)