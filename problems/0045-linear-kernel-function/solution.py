import numpy as np

def kernel_function(x1, x2):
	# Your code here
	return sum(i * j for i, j in zip(x1, x2))
