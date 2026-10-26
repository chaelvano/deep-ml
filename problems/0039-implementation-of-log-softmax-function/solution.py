import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	# Your code here
	log_softmax = np.empty(len(scores))
	exp_sum = 0

	for score in scores:
		exp_sum += np.exp(score)

	for i in range(len(scores)):
		log_softmax[i] = scores[i] - np.log(exp_sum)

	return log_softmax