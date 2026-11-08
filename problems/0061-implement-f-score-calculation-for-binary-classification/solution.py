import numpy as np

def f_score(y_true, y_pred, beta):
	"""
	Calculate F-Score for a binary classification task.

	:param y_true: Numpy array of true labels
	:param y_pred: Numpy array of predicted labels
	:param beta: The weight of precision in the harmonic mean
	:return: F-Score rounded to three decimal places
	"""
	# 2TP / (2TP + FP + FN)
	tp = sum(1 if p == 1 and p == l else 0 for p, l in zip(y_pred, y_true))
	fp = sum(1 if p == 1 and p != l else 0 for p, l in zip(y_pred, y_true))
	fn = sum(1 if p == 0 and p != l else 0 for p, l in zip(y_pred, y_true))

	precision = tp / (tp + fp)
	recall = tp / (tp + fn)

	f_beta = (1 + beta ** 2) * precision * recall / (beta ** 2 * precision + recall)

	return round(f_beta, 3)
