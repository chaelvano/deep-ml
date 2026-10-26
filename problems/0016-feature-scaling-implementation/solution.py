import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here
	standardized_data = [[] for _ in range(len(data))]
	normalized_data = [[] for _ in range(len(data))]

	for j in range(len(data[0])):
		col_sum = 0
		col_squared_sum = 0

		col_min = float('inf')
		col_max = float('-inf')

		# First pass - Gather statistics
		for i in range(len(data)):
			x = data[i][j]

			col_sum += x
			col_squared_sum += x ** 2

			if x < col_min:
				col_min = x

			if x > col_max:
				col_max = x

		col_mean = col_sum / len(data)
		col_std = ((col_squared_sum / len(data)) - (col_mean) ** 2) ** 0.5

		col_range = col_max - col_min

		# Second pass - Scale
		for i in range(len(data)):
			standardized_data[i].append((data[i][j] - col_mean) / col_std)

			normalized_data[i].append((data[i][j] - col_min) / col_range)

	return standardized_data, normalized_data