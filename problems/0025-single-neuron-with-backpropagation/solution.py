import numpy as np
def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
	# Your code here
	n = features.shape[0]

	updated_weights = initial_weights
	updated_bias = initial_bias
	mse_values = np.zeros(epochs)

	for e in range(epochs):
		weights_d_mse = np.zeros(updated_weights.shape[0])
		bias_d_mse = 0

		for i in range(n):
			z = sum(w * x for w, x in zip(updated_weights, features[i])) + updated_bias
			activation = 1 / (1 + np.exp(-z))
			d_activation = activation * (1 - activation)
			error = activation - labels[i]
			weights_d_mse += 2 * error * d_activation * features[i] / n 
			bias_d_mse += 2 * error * d_activation / n 
			mse_values[e] += np.square(error) / n

		updated_weights -= learning_rate * weights_d_mse
		updated_bias -= learning_rate * bias_d_mse

	return updated_weights, updated_bias, mse_values