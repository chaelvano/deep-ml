import numpy as np

def accuracy_score(y_true, y_pred):
	# Your code here
	acc = 0

	for i in range(len(y_pred)):
		if y_pred[i] == y_true[i]:
			acc += 1 / len(y_pred)

	return acc