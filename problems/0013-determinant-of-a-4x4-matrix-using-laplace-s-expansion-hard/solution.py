def determinant_4x4(matrix: list[list[int|float]]) -> float:
	# Your recursive implementation here
	# The problem asked for the recursive approach
	m = len(matrix)

	if m == 1:
		return matrix[0][0]

	if m == 2:
		return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

	det = 0

	# Expand along the first column (or any row/column, ideally the one with most zeros) 
	for i in range(m):
		minor = [row[1:] for row in matrix[:i] + matrix[i + 1:]]
		det += (-1) ** i * matrix[i][0] * determinant_4x4(minor)

	return det