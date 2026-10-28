import numpy as np

def recall(y_true, y_pred):
    """
    Calculate the recall metric for binary classification.
    
    Args:
        y_true: Array of true binary labels (0 or 1)
        y_pred: Array of predicted binary labels (0 or 1)
    
    Returns:
        Recall value as a float
    """
    # Your code here
    if sum(y_true) == 0:
        return 0

    return sum([1 if a == 1 and b == 1 else 0 for a, b in zip(y_true, y_pred)]) / sum(y_true)
