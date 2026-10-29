import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	return sum([a * b for a, b in zip(v1, v2)]) / (np.sqrt(sum([a ** 2 for a in v1])) * np.sqrt(sum([a ** 2 for a in v2])) )