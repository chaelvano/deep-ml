def min_max(x: list[float]) -> list[float]:
    """
    Perform Min-Max normalization to scale values to [0, 1].
    
    Args:
        x: A list of numerical values
    
    Returns:
        A new list with values normalized to [0, 1]
    """
    # Your code here
    x_min = min(x)
    x_max = max(x)

    if x_min == x_max:
        return [0] * len(x)

    min_max_scaled = []

    for i in x:
        min_max_scaled.append((i - x_min) / (x_max - x_min))

    return min_max_scaled