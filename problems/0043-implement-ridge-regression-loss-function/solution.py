import numpy as np

def ridge_loss(X: np.ndarray, weights: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
	# Your code here
	preds = [sum(x * w for x, w in zip(X[i], weights)) for i in range(len(X))]
	mse = sum((yt - yp) ** 2 for yt, yp in zip(y_true, preds)) / len(X)

	sq_norm = sum(w ** 2 for w in weights)
	reg = alpha * sq_norm

	return mse + reg