def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	result = []

	for i in range(len(matrix)):
		row = []

		for j in range(len(matrix[0])):
			row.append(scalar * matrix[i][j])

		result.append(row)

	return result