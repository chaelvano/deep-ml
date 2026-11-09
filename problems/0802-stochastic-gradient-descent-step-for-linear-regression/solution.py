import numpy as np

def sgd_update(X: np.ndarray, y: np.ndarray, weights: np.ndarray, learning_rate: float, n_iter: int) -> list:
    """
    Perform n_iter steps of stochastic gradient descent on a linear regression
    model with MSE loss, cycling through samples in order.

    Returns the final weight vector as a Python list.
    """
    weights = np.array(weights, dtype=float)
    N = X.shape[0]

    for i in range(n_iter):
        idx = i % N

        pred = X[idx] @ weights
        err = pred - y[idx]
        loss = err * err

        # dL/dw_j = dL/de * de/dy_hat * dy_hat/dw_j
        # dL/dw_j = 2e * 1 * x_j
        grad = 2 * err * X[idx]
        weights -= learning_rate * grad

    return weights.tolist()