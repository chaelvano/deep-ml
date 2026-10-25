def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	if len(a[0]) != len(b):
		return -1

	result = []

	for row in a:
		row_result = 0

		for i in range(len(row)):
			row_result += row[i] * b[i]

		result.append(row_result)

	return result