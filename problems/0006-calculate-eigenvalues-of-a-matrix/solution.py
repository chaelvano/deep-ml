def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	# 2x2 constraint
	trace = matrix[0][0] + matrix[1][1]
	det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
	eigenvalues = [(trace + (trace ** 2 - 4 * det) ** (1 / 2)) / 2, (trace - (trace ** 2 - 4 * det) ** (1 / 2)) / 2]

	eigenvalues.sort(reverse=True)

	return eigenvalues