import numpy as np

def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # TODO: Implement the function
    n = len(samples)
    values, counts = np.unique(samples, return_counts=True)
    probabilities = map(lambda x: x / n, counts)

    return [(value, probability) for value, probability in zip(values, probabilities)]