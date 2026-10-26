import numpy as np

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	# Your code here
	probabilities = []
	squared_errors = 0

	for i in range(len(features)):
		logit = bias

		for j in range(len(features[0])):
			logit += weights[j] * features[i][j]

		probabilities.append(1 / (1 + np.exp(-logit)))

		squared_errors += (probabilities[i] - labels[i]) ** 2

	mse = squared_errors / len(features)

	return probabilities, mse