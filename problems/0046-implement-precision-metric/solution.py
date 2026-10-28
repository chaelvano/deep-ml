import numpy as np
def precision(y_true, y_pred):
	# Your code here
	if sum(y_pred) == 0:
		return 0

	return sum(1 if a == 1 and b == 1 else 0 for a, b in zip(y_true, y_pred)) / sum(y_pred)
