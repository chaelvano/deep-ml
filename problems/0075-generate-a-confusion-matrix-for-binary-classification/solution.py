from collections import Counter

def confusion_matrix(data):
	# Implement the function here
	counts = Counter(map(tuple, data))

	return [[counts[(1, 1)], counts[(1, 0)]], [counts[(0, 1)], counts[(0, 0)]]]
