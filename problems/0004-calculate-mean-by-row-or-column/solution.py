def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []

	if mode == "row":
		for i in range(len(matrix)):
			row = 0

			for j in range(len(matrix[0])):
				row += matrix[i][j]

			means.append(row / len(matrix[0]))

	elif mode == "column":
		for i in range(len(matrix[0])):
			column = 0

			for j in range(len(matrix)):
				column += matrix[j][i]

			means.append(column / len(matrix))

	return means