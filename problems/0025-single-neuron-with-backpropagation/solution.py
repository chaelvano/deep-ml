import numpy as np
def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
	# Your code here
	n = features.shape[0]

	updated_weights = initial_weights
	updated_bias = initial_bias
	mse_values = np.zeros(epochs)

	for e in range(epochs):
		z = np.dot(features, updated_weights) + updated_bias
		sigmoid = 1 / (1 + np.exp(-z))
		error = sigmoid - labels

		updated_weights -= learning_rate * 2 * np.dot(features.T, error * sigmoid * (1 - sigmoid)) / n
		updated_bias -= learning_rate * 2 * np.sum(error * sigmoid * (1 - sigmoid)) / n
		mse_values[e] = np.sum(np.square(error)) / n

	return updated_weights, updated_bias, mse_values