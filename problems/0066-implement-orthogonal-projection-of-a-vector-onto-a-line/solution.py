def orthogonal_projection(v, L):
	"""
	Compute the orthogonal projection of vector v onto line L.

	:param v: The vector to be projected
	:param L: The line vector defining the direction of projection
	:return: List representing the projection of v onto L
	"""
	L_length = sum(i ** 2 for i in L) ** (1 / 2)
	L_hat = [i / L_length for i in L]

	return [m * n * n for m, n in zip(v, L_hat)]