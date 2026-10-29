import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    # Your code here
    arr = arr.astype(float)

    if norm_type == "l1":
        return sum([np.abs(x) for x in arr.flatten()])
    
    elif norm_type == "l2":
        return np.sqrt(sum([x ** 2 for x in arr.flatten()]))
    
    elif norm_type == "linf":
        return np.abs(arr.flatten()).max()

    elif norm_type == "frobenius":
        if arr.ndim != 2:
            raise ValueError()

        return np.sqrt(sum([np.abs(x) ** 2 for x in arr.flatten()]))
