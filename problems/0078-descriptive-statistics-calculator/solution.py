import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    # Your code here
    # I'm not sure whether I'm supposed to compute them manually or use NumPy. I'll just assume the later
    mean = np.mean(data)
    median = np.median(data)
    var = np.var(data)
    std = np.std(data)
    q1 = np.quantile(data, 0.25)
    q2 = np.quantile(data, 0.5)
    q3 = np.quantile(data, 0.75)
    iqr = q3 - q1

    values, counts = np.unique(data, return_counts=True)
    mode = values[np.argmax(counts)]

    return {
        "mean": mean,
        "median": median,
        "mode": mode,
        "variance": var,
        "standard_deviation": std,
        '25th_percentile': q1, 
        '50th_percentile': q2, 
        '75th_percentile': q3, 
        'interquartile_range': iqr
    }