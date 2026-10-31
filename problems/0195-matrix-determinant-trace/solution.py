# There is no constraint defined for the matrix size
def determinant(matrix):
	m = len(matrix)
	A = [row[:] for row in matrix] # creates a copy of the matrix
	det = 1

	for i in range(m):
		pivot = max(range(i, m), key=lambda r: abs(A[r][i])) # find the row with the largest value of column i

		if A[pivot][i] == 0:
			return 0

		# Row swap
		if pivot != i:
			A[i], A[pivot] = A[pivot], A[i]
			det *= -1

		det *= A[i][i]

		# Subtract a row with a multiple of row i
		for r in range(i + 1, m):
			factor = A[r][i] / A[i][i]

			for c in range(i + 1, m):
				A[r][c] -= factor * A[i][c]

			A[r][i] = 0

	return det

def trace(matrix):
	return sum(matrix[i][i] for i in range(len(matrix)))

def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
	"""
	Compute the determinant and trace of a square matrix.
	
	Args:
		matrix: A square matrix (n x n) represented as list of lists
	
	Returns:
		Tuple of (determinant, trace)
	"""
	# Your code here
	# return(np.linalg.det(matrix), np.trace(matrix))
	return (determinant(matrix), trace(matrix))