import numpy as np

def rmse(y_true, y_pred):
	# Write your code here
	return round(np.sqrt(np.mean(np.square(y_true - y_pred))), 3)